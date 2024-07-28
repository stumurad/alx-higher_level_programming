#!/usr/bin/python3
import sys
import hidden_4
if __name__ == "__main__":

    name = dir(hidden_4.pyc)
filtered_names = [name for name in names if not name.startswith("__")]

for name in filtered_names:
    print(name)
