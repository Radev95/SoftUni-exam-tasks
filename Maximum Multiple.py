divider = int(input())
divisor = int(input())
for number in range(divisor, -1, -1):
    if number % divider == 0:
        break
print(f'{number}')
