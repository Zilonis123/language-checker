import subprocess, json
from termcolor import colored

def check_language_installation(language_info: dict) -> bool:
    try:
        execute_command = " ".join(language_info["execute"])
        subprocess.run(execute_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    # Load JSON file
    with open("checks.json", "r") as json_file:
        data: dict = json.load(json_file)

    found_langs = []

    # Check each language
    for language_info in data["checks"]:
        found: bool = check_language_installation(language_info)
        if found:
            found_langs.append(language_info["language"])
        # clearconsole()

    # Display results
    color = colored("+", "green")
    for lang in found_langs:
        print(f"{color} {lang.capitalize()}")

if __name__ == "__main__":
    main()