def get_letter(score):  # function converts scores from 0 to 1 to letter grades 
    if score >= 0.9:
        return('A')
    elif score >= 0.8:
        return('B')
    elif score >= 0.7:
        return('C')
    elif score >= 0.6:
        return('D')
    elif score >= 0:
        return('F')
    else:
        return('invalid_score')


with open('student_scores.csv') as f:  # read input into list of strings
    student_input = f.readlines()

student_output = []
for line in student_input:
    student_data = line.strip('\n').split('\t')  # parse the row from the csv into a list. first element is name, second element is score
    student_name = student_data[0]
    student_score = student_data[1]
    student_letter = get_letter(student_score)  # convert student score to letter grade, by calling function
    newline = student_name + ',' + student_letter + '\n'  # create output line with student's name and letter grade
    student_output.append(newline)

with open('student_letters.csv', 'w') as f:  # write output
    f.writelines(student_output)
