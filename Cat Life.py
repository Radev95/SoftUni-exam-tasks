cat_type = input()
gender = input()

life = 0
if gender == "m":
    if cat_type == "British Shorthair":
        life: float = (13 * 12) / 6
        print(f"{life :.0f} cat months")
    elif cat_type == "Siamese":
        life = (15 * 12) / 6
        print(f"{life:.0f} cat months")
    elif cat_type == "Persian":
        life = (14 * 12) / 6
        print(f"{life:.0f} cat months")
    elif cat_type == "Ragdoll":
        life = (16 * 12) / 6
        print(f"{life:.0f} cat months")
    elif cat_type == "American Shorthair":
        life = (12 * 12) / 6
        print(f"{life:.0f} cat months")
    elif cat_type == "Siberian":
        life = (11 * 12) / 6
        print(f"{life:.0f} cat months")
    else:
        print(f"{cat_type} is invalid cat!")
elif gender == "f":
    if cat_type == "British Shorthair":
        life = (14 * 12) / 6
        print(f"{life:.0f} cat months")
    elif cat_type == "Siamese":
        life = (16 * 12) / 6
        print(f"{life:.0f} cat months")
    elif cat_type == "Persian":
        life = (15 * 12) / 6
        print(f"{life:.0f} cat months")
    elif cat_type == "Ragdoll":
        life = (17 * 12) / 6
        print(f"{life:.0f} cat months")
    elif cat_type == "American Shorthair":
        life = (13 * 12) / 6
        print(f"{life:.0f} cat months")
    elif cat_type == "Siberian":
        life = (12 * 12) / 6
        print(f"{life:.0f} cat months")
    else:
        print(f"{cat_type} is invalid cat!")
