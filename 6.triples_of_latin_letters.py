a = int(input())
for i in range(0,a):
    for j in range(0,a):
        for k in range(0,a):
            print(f"{chr(97+i)}{chr(97+j)}{chr(97+k)}")
