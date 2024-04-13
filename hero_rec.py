def enroll(heroes, hero_name):
    if hero_name not in heroes:
        heroes[hero_name] = []
    else:
        print(f"{hero_name} is already enrolled.")


def learn(heroes, hero_name, spell_name):
    if hero_name in heroes:
        if spell_name not in heroes[hero_name]:
            heroes[hero_name].append(spell_name)
        else:
            print(f"{hero_name} has already learnt {spell_name}.")
    else:
        print(f"{hero_name} doesn't exist.")


def unlearn(heroes, given_name, spell):
    if given_name in heroes:
        if spell in heroes[given_name]:
            heroes[given_name].remove(spell)
        else:
            print(f"{given_name} doesn't know {spell}.")
    else:
        print(f"{given_name} doesn't exist.")


def print_heroes(heroes):
    print("Heroes:")
    for hero, spells in heroes.items():
        print(f"== {hero}: {', '.join(spells)}")


def main():
    heroes = {}

    while True:
        command = input().split()
        if command[0] == 'End':
            break
        elif command[0] == 'Enroll':
            hero_name = command[1]
            enroll(heroes, hero_name)
        elif command[0] == 'Learn':
            hero_name, spell_name = command[1], command[2]
            learn(heroes, hero_name, spell_name)
        elif command[0] == 'Unlearn':
            hero_name, spell_name = command[1], command[2]
            unlearn(heroes, hero_name, spell_name)

    print_heroes(heroes)


if __name__ == "__main__":
    main()
