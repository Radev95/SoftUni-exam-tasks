the_goal = int(input())
jump = int(input())
height_to_be_jumped = the_goal - 30
failed_jumps = 0
jumps_counter = 0
flag = False

while height_to_be_jumped <= the_goal:
    if jump > height_to_be_jumped:
        jumps_counter += 1
        if height_to_be_jumped >= the_goal:
            break
        height_to_be_jumped += 5
        failed_jumps = 0
    else:
        jumps_counter += 1
        failed_jumps += 1
        if failed_jumps == 3:
            print(f"Tihomir failed at {height_to_be_jumped}cm after {jumps_counter} jumps.")
            flag = True
            break
    jump = int(input())
if not flag:
    print(f"Tihomir succeeded, he jumped over {height_to_be_jumped}cm after {jumps_counter} jumps.")