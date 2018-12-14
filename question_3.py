# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.

def get_divisible_by_5():
    seq = raw_input("Enter comma separated sequence: ")
    seq_list = seq.split(',')
    my_output = ""
    for number in seq_list:
        if int(number)%5 == 0:
            my_output +=  number + ", "
    print(my_output)

get_divisible_by_5()
