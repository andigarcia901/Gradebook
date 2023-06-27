
# Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

def get_grade(s1, s2, s3):
    average = (s1 + s2 + s3)/3.0
    if average <= 100 or average >= 90:
        return "A"
    # elif 80 >= average <= 90:
    #     return "B"
    # elif 70>= average <= 80:
    #     return "C"
    # elif 60 >= average <= 70:
    #     return "D"
    else: 
       return "F"
    
student_one = get_grade(90, 95, 97)
print(student_one)

student_two = get_grade(88, 75, 91)
print(student_two)