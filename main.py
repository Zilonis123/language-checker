import subprocess, json
from termcolor import colored

def check_language_installation(exec: list[str]) -> bool:
    try:
        execute_command: str = " ".join(exec)
        subprocess.run(execute_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    # Load JSON file
    with open("checks.json", "r") as json_file:
        data: dict = json.load(json_file)


    plus: str = colored("+", "green")
    # Check each language
    for language_info in data["checks"]:
        found: bool = check_language_installation(language_info["execute"])

        if not found and language_info.get("execute2", False):
            # in some cases languages may differ between operating systems
            found: bool = check_language_installation(language_info["execute2"])

        if found:
            # Display results
            lang: str = language_info["language"].capitalize()
            print(f"{plus} {lang}")

if __name__ == "__main__":
    main()