# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.


def divisible_by_7_btn_2000_3200_included():
    divisible_by_7_list = []
    for i in range(2000, 3201):
        if i%7 == 0:
            divisible_by_7_list.append(i)
    print(divisible_by_7_list)

divisible_by_7_btn_2000_3200_included()
            