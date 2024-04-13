list_of_names = input().split(", ")
command = input().split(" ")
blacklist = 0
lost = 0
while command[0] != "Report":
    change = command[0]
    name = command[1]
    if change == "Blacklist":
        if name in list_of_names:
            blacklist += 1
            name_index = list_of_names.index(name)
            print(f"{name} was blacklisted.")
            list_of_names[name_index] = "Blacklisted"
        else:
            print(f"{name} was not found.")
    elif change == "Error":
        if 0 <= int(name) <= len(list_of_names) - 1:
            current_index = 0
            step = int(name)
            current_index += step
            if (not (not (list_of_names[current_index] != "Lost") or not (
                    list_of_names[current_index] != "Blacklisted") or not (
                    0 <= current_index <= len(list_of_names) - 1))):
                print(f"{list_of_names[current_index]} was lost due to an error.")
                lost += 1
                list_of_names[current_index] = "Lost"
    elif change == "Change":
        if 0 <= int(name) <= len(list_of_names) - 1:
            current_index = 0
            step = int(name)
            current_index += step
            new_name = command[2]
            if 0 <= current_index <= len(list_of_names) - 1:
                print(f"{list_of_names[current_index]} changed his username to {new_name}.")
            list_of_names[current_index] = new_name

    command = input().split(" ")

print(f"Blacklisted names: {blacklist}")
print(f"Lost names: {lost}")
print(" ".join(list_of_names))
