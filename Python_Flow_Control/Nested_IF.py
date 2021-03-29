# 80 to 100 = distinstin
# 60 to 79 = First Class
# 50 to 59 = Second Class
# 35 to 49 = Pass
# < 35 = fail

num = 34
Max_Marks = 100

if num <= Max_Marks | num >= 0:

    if num >= 80 & 80 <= Max_Marks:
        print(num, " Distinction")

    elif num > 59 & num < 80:
        print(num, "First Class")

    elif num > 49 & 49 < 60:
        print(num, "Second Class")

    elif num > 34 & 35 <= 50:
        print(num, "Pass")

    elif num < 35:
        print (num, "Fail")
else:
    print("Invalid Number")
