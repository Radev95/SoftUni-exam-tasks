import math
budget = float(input())
students = int(input())
price_for_a_package_of_flour = float(input())
price_for_a_single_egg = float(input())
price_for_a_single_apron = float(input())

apron_price_total = price_for_a_single_apron * math.ceil(students * 1.2)
egg_price_total = price_for_a_single_egg * students * 10
if 5 <= students < 10:
    flour_price_total = price_for_a_package_of_flour * (students - 1)
elif 10 <= students < 15:
    flour_price_total = price_for_a_package_of_flour * (students - 2)
elif 15 <= students < 20:
    flour_price_total = price_for_a_package_of_flour * (students - 3)
elif 20 <= students < 25:
    flour_price_total = price_for_a_package_of_flour * (students - 4)
elif 25 <= students < 30:
    flour_price_total = price_for_a_package_of_flour * (students - 5)
else:
    flour_price_total = price_for_a_package_of_flour * students

total_price = apron_price_total + egg_price_total + flour_price_total
if total_price <= budget:
    print(f"Items purchased for {total_price:.2f}$.")
else:
    print(f"{total_price - budget:.2f}$ more needed.")
