first = input()
second = input()
last_print = first
for character_index in range (len(first)):
    left = second[:character_index + 1]
    right = first[character_index + 1:]
    new = left + right
    if new != last_print:
        print(new)
        last_print = new
