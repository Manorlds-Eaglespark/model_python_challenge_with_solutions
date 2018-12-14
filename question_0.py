# Make a grading system for the students marks below
# [23,4,5,6,64,90,67,98,45,23,67,78,89]
# Create two lists and add numbers greater than 50 and another list for numbers less than 50
# And show an appropriate message for his mark


def grading_system(marks_list):

    above_average = []
    below_average = []

    for mark in marks_list:
        if mark < 50:
            below_average.append(mark)
        else:
            above_average.append(mark)

    print("-"*50)
    print("Above Average List: "+ str(above_average))
    print("-"*50)
    for mark in above_average:
        if mark > 90:
            print(str(mark)+" is Excellent.")
        elif mark < 90 and mark > 69:
            print(str(mark)+" is Very Good.")
        elif mark < 70 and mark > 59:
            print(str(mark)+" is Good.")
    print("+"*50)
    print("Below Average List: "+ str(below_average))
    print("-"*50)
    for mark in below_average:
        if mark < 60 and mark > 39:
            print(str(mark)+" is Poor.")
        elif mark < 40 and mark > 19:
            print(str(mark)+" is Very Poor.")
        elif mark > 20:
            print(str(mark)+" - Repeat.")
    


grading_system([23,4,5,6,64,90,67,98,45,23,67,78,89])