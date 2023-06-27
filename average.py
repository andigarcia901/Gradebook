
# Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

def get_grade(s1, s2, s3):
    average = (s1 + s2 + s3)/3.0
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else: 
       return "F"
    
student_one = get_grade(90, 95, 97) # average is 94, should print A
print(student_one)

student_two = get_grade(88, 75, 91) # average is 84.6, should print B
print(student_two)

student_three = get_grade(63, 86, 72) 
print(student_three)