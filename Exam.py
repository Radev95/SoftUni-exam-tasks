number_of_students = int(input())
results_t = 0
top_st = 0
umid = 0
lmid = 0
failed = 0

for i in range(number_of_students):
    result = float(input())
    if result >= 5:
        results_t += result
        top_st += 1
    elif 4 <= result <= 4.99:
        results_t += result
        umid += 1
    elif 3 <= result <= 3.99:
        results_t += result
        lmid += 1
    elif result <= 2.99:
        results_t += result
        failed += 1

average = results_t / number_of_students
top = top_st / number_of_students * 100
uppermid = umid / number_of_students * 100
lowermid = lmid / number_of_students * 100
failure = failed / number_of_students * 100

print(f"Top students: {top:.2f}%")
print(f"Between 4.00 and 4.99: {uppermid:.2f}%")
print(f"Between 3.00 and 3.99: {lowermid:.2f}%")
print(f"Fail: {failure:.2f}%")
print(f"Average: {average:.2f}")