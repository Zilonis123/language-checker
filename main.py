# import the dependencies
import os
import json
from termcolor import colored

checks = [
    {
        "language": "python",
        "execute": "python --version"
    },
    {
        "language": "node.js",
        "execute": "node --version"
    },
    {
        "language": "c++",
        "execute": "g++ -v"
    }
]


for check in checks:
    # steps
    # 1. execute the command
    # 2. check if the command didn't return an error
    # 2.1 it didn't - print that the system has the code language installed
    # 2.2 it did - check if the user wants the not found languages to be printed if does print

    # 1.
    res = os.popen(check["execute"], "r", 0)

    # 2.
    if res.close():
        # 2.2
        continue;

    # 2.1
    color = colored(check["language"], "green")
    print("[ "+ color + " ]")