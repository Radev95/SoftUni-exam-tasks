from collections import Counter

def count_letter(text):
    text = ''.join(text)
    chars_dict = Counter(text)

    return chars_dict


text = input().split()
characters_dictionary = count_letter(text)

for k, v in characters_dictionary.items():
    print(f'{k} -> {v}')