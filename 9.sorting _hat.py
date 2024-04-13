name = input()

for character_input in range(len(name)):
    if name == "Voldemort":
        print("You must not speak of that name!")
        break
    if name == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    else:
        print(f"{name} goes to Hufflepuff.")
    next_name = input()
    name = next_name
