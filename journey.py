budget = float(input())
season = input()
place = ""
type_trip = ""
spend_sum = 0

if budget <= 100:
    type_trip = "Bulgaria"
    if season == "summer":
        spend_sum = budget * 0.3
    elif season == "winter":
        spend_sum = budget * 0.7

elif budget <= 1000:
    type_trip = "Balkans"
    if season == "summer":
        spend_sum = budget * 0.4

    elif season == "winter":
        spend_sum = budget * 0.8
else:
    type_trip = "Europe"
    spend_sum = budget * 0.9
    place = "Hotel"
if season == "summer" and type_trip != "Europe":
    place = "Camp"
else:
    place = "Hotel"

print(f"Somewhere in {type_trip}")
print(f"{place} - {spend_sum:.2f}")