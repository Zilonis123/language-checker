import subprocess, json, argparse
from termcolor import colored

def check_language_installation(exec: list[str]) -> bool:
    try:
        execute_command: str = " ".join(exec)
        subprocess.run(execute_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def background_check(args, data: dict):

    plus: str = colored("+", "green")
    minus: str = colored("-", "red")

    for language_info in data["checks"]:
        found: bool = check_language_installation(language_info["execute"])

        if not found and language_info.get("execute2", False):
            # in some cases languages may differ between operating systems
            found: bool = check_language_installation(language_info["execute2"])


        lang: str = language_info["language"].capitalize()

        if found and not args.onlynotfound:
            print(f"{plus} {lang}")
        elif args.notfound or args.onlynotfound:
            print(f"{minus} {lang}")

def oneline_check(args, data: dict):
    found = []
    notfound = []
    for language_info in data["checks"]:
        f: bool = check_language_installation(language_info["execute"])

        if not f and language_info.get("execute2", False):
            # in some cases languages may differ between operating systems
            f: bool = check_language_installation(language_info["execute2"])
        
        lang: str = language_info["language"].capitalize()

        if f:
            found.append(lang)
        else:
            notfound.append(lang)


    plus: str = colored("+", "green")
    minus: str = colored("-", "red")


    if found and not args.onlynotfound:
        langs = ", ".join(found)
        print(f"{plus} {langs}")
    
    if args.notfound or args.onlynotfound:
        langs = ", ".join(notfound)
        print(f"{minus} {langs}")

def main():

    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Check if programming languages are installed.")
    parser.add_argument("-s", "--sort", action="store_true", help="Sort the data alphabetically")
    parser.add_argument("-nf", "--notfound", action="store_true", help="Print the languages that weren't found")
    parser.add_argument("-onf", "--onlynotfound", action="store_true", help="ONLY print the languages that weren't found")
    parser.add_argument("-o", "--oneline", action="store_true", help="Prints all the languages in oneline")
    args = parser.parse_args()


    # Load JSON file
    with open("checks.json", "r") as json_file:
        data: dict = json.load(json_file)

    # sort the data
    if args.sort:
        data["checks"] = sorted(data["checks"], key=lambda x: x['language'])


    # Check each language
    if not args.oneline:
        background_check(args, data)
    else:
        oneline_check(args, data)

if __name__ == "__main__":
    main()