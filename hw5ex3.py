import csv

def find_matches(favorite, catagory):  # function to find all students whose favorite item in a catagory matches the input choice
    agreeing_students = []
    for student in student_data:
        if student[catagory]==favorite:
            agreeing_students.append(student['Name'])
    if agreeing_students:
        print('These students agree with you:')
        print(agreeing_students)
    else:
        print('That was a unique choice')


with open('student_favorites.csv') as f:  # read file. parse as a list (each element is a row) of dictionaries (each key is a column)
    student_data = []
    for row in csv.DictReader(f):
        student_data.append(row)

fav_color = input('What is your favorite color? ')  # ask the user for a color. find all students who have that favorite color. 
find_matches(fav_color, 'Color')

fav_fruit = input('What is your favorite fruit? ')  # again, but for favorite fruit
find_matches(fav_fruit, 'fruit')

fav_flower = input('What is your favorite flower? ')  # again, but for favorite flower
find_matches(fav_fruit, 'Flower')