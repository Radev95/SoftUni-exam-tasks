import math
budget = float(input())
students = int(input())
price_for_a_package_of_flour = float(input())
price_for_a_single_egg = float(input())
price_for_a_single_apron = float(input())
apron_price_total = price_for_a_single_apron * math.ceil(students * 1.2)
egg_price_total = price_for_a_single_egg * students * 10
flour_discount = int(students / 5)
flour_price_total = price_for_a_package_of_flour * (students - flour_discount)
total_price = apron_price_total + egg_price_total + flour_price_total
if total_price <= budget:
    print(f"Items purchased for {total_price:.2f}$.")
else:
    print(f"{total_price - budget:.2f}$ more needed.")
