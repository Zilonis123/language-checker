import subprocess, json
from termcolor import colored

def check_language_installation(language_info: dict) -> bool:
    try:
        execute_command: str = " ".join(language_info["execute"])
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
        found: bool = check_language_installation(language_info)

        if found:
            # Display results
            lang: str = language_info["language"].capitalize()
            print(f"{plus} {lang}")

if __name__ == "__main__":
    main()