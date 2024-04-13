word = input()

while True:
    commands = input()
    command = commands.split()[0]
    if command == "Finish":
        break

    elif commands == 'Make Upper':
        word = word.upper()
        print(word)

    elif commands == 'Make Lower':
        word = word.lower()
        print(word)

    elif command == 'Replace':
        letter = commands.split()[1]
        new_letter = commands.split()[2]
        word = word.replace(letter, new_letter)
        print(word)

    elif command == 'Check':
        if commands.split()[1] in word:
            print(f"Message contains {commands.split()[1]}")
        else:
            print(f"Message doesn't contain {commands.split()[1]}")

    elif command == 'Cut':
        index_a = commands.split()[1]
        index_b = commands.split()[2]
        index_1 = int(index_a)
        index_2 = int(index_b)
        if index_1 < 0 or index_2 >= len(word):
            print("Invalid indices!")
        else:
            word = word[:index_1] + word[index_2 + 1:]
            print(word)

    elif command == 'Sum':
        index_a = commands.split()[1]
        index_b = commands.split()[2]
        index_1 = int(index_a)
        index_2 = int(index_b)
        if index_1 < 0 or index_2 >= len(word):
            print("Invalid indices!")
        else:
            sum_word = word[index_1:index_2 + 1]
            ascii_sum = sum(ord(char) for char in sum_word)
            print(ascii_sum)
