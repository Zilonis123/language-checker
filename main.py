# import the dependencies
import subprocess
import json
from termcolor import colored
from cli_args_system import Args



def main():
    args = Args(convert_numbers=False)

    onlyFound = bool(args.flags_names("o"))


    with open("checks.json", "r", encoding="utf-8") as data_file:
        checks = json.load(data_file).get("checks")

    found = []
    notfound = []
    for check in checks:
        # steps
        # 1. execute the command
        # 2. check if the command didn't return an error
        # 2.1 it didn't - add the found language to the list
        # 2.2 it did - add the found to the notfound

        # 1.
        res = subprocess.run(check["execute"], shell=True)

        # clear the terminal
        subprocess.run(["cls"], shell=True)
        # 2.
        if res.returncode == 1:
            # 2.2
            notfound.append(check["language"])
            continue;

        # 2.1
        found.append(check["language"])

    for language in sorted(found):
        color = colored("+", "green")
        print("[" + color + "] " + language.capitalize() + " was found.")

    if not onlyFound:
        for language in sorted(notfound):
            color = colored("-", "red");
            print("[" + color + "] " + language.capitalize() + " was NOT found.")

if __name__ == "__main__":
    main()