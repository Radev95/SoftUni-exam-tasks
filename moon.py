import math
from math import ceil

avg_speed = float(input())
fuel_per_100km = float(input())

distance = 384400 * 2

print(f"{((math.ceil(distance / avg_speed))+3)}")
print(f"{((fuel_per_100km * distance) / 100):.0f}")
