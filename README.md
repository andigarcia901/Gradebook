# Gradebook
Function to find the average of 3 scores and print the letter value associated with that score

Wrote the whole function in a way I thought would work and then began going back to problem solve.

-I made a practice student_one and student_two.  Mathematically, they should return two different letter grades but in the function they are returning the same letter.  

-Found solution:  I was improperly using "or".  To solve the error, I removed using "or" between the number ranges and simplified by just using one grater than sign.