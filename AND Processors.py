import math
from math import floor

processors = int(input())
people = int(input())
days = int(input())

all_hours_work = days * people * 8
total_processors = math.floor(all_hours_work / 3)
revenue = abs((processors - total_processors) * 110.10)

if total_processors >= processors:
    print(f"Profit: -> {revenue:.2f} BGN")
else:
    print(f"Losses: -> {revenue:.2f} BGN")
