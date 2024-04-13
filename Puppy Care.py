food_quantity = int(input()) * 1000
food_consumed = 0

while True:
    i = input()
    if i == "Adopted":
        break
    else:
        food_consumed += int(i)

food = abs(food_consumed - food_quantity)

if food_quantity >= food_consumed:
    print(f"Food is enough! Leftovers: {food} grams." )
else:
    print(f"Food is not enough. You need {food} grams more.")
