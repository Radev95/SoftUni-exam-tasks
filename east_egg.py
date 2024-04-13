import re


def find_eggs(text):
    pattern = r'[@#]+([a-z]{3,})[^a-zA-Z\d]*\/(\d+)\/'
    matches = re.findall(pattern, text)
    for color, element in matches:
        print(f"You found {element} {color} eggs!")


def main():
    text = input()
    find_eggs(text)


if __name__ == "_main_":
    main()
