number_of_locations = int(input())

for d in range(number_of_locations):
    expected_avg = float(input())
    days_at_location = int(input())
    total_at_location = 0
    for e in range(days_at_location):
        gold_per_day = float(input())
        total_at_location += gold_per_day

    total_average = total_at_location / days_at_location
    gold = abs(expected_avg - total_average)

    if total_average >= expected_avg:
        print(f"Good job! Average gold per day: {total_average:.2f}.")
    else:
        print(f"You need {gold:.2f} gold.")







