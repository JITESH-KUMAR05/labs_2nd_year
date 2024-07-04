math_marks = float(input("Enter math marks: "))
physics_marks = float(input("Enter physics marks: "))
chemistry_marks = float(input("Enter chemistry marks: "))
total_marks = math_marks + physics_marks + chemistry_marks
average = total_marks/3
# print("Total marks: ", total_marks)

if((math_marks<0 or math_marks>100) or (physics_marks<0 or physics_marks>100) or (chemistry_marks<0 or chemistry_marks>100)):
    print("Invalid marks entered")
else:
    print(f"your average is {average}")
    if(average>98):
        print("Eligible for Scholarship")
    else:
        print("Not Eligible for Scholarship")