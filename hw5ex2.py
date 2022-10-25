with open('flowers.txt') as f:  # read input into list of strings
    input_flowers = f.readlines()

for flower in input_flowers:
    flower_data = flower.strip('\n').split('\t')  # parses line into a list. first element is the student's name. second element is their favorite flower
    name = flower_data[0]
    favorite_flower = flower_data[0]
    fav_flowers[name] = favorite_flower  # converts list into element of a dictionary. Key is the student's name. Value is the student's favorite flower.

student_of_interest = input('Enter students name: ')
print(fav_flowers.get(student_of_interest, 'Student not found'))