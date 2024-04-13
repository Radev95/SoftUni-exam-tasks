n = int(input())
v = 0
for i in range(n):
    incoming = int(input())
    if v + incoming <= 255:
        v += incoming
    else:
        print("Insufficient capacity!")
print(v)
