#!/usr/bin/python3
"""Adds all arguments to list"""


if __name__ == "__main__":
    from sys import argv
    save = __import__('5-save_to_json_file').save_to_json_file
    load = __import__('6-load_from_json_file').load_from_json_file

    data = []
    try:
        data = load("add_item.json")
        for item in argv[1:]:
            data.append(item)
        save(data, "add_item.json")
    except FileNotFoundError:
        for item in argv[1:]:
            data.append(item)
        save(data, "add_item.json")
