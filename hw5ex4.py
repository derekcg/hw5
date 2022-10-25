import argparse

def get_popular(favorites): # input is a list. Prints the most commonly repeated element in the list.
    counts = {}
    for favorite in favorites:
        counts[favorite] = counts.get(favorite, 0) + 1
    most_popular = max(counts, key=counts.get)
    print('Most Popular Favorite: ', most_popular)

# interpret user options to determine which file to read
parser = argparse.ArgumentParser(description='Find Most Popular Favorites')
parser.add_argument('-i', '--infile', help='input file with student favorite things in multiple catagories', default='student_favorites.csv')
args = parser.parse_args()

# read file. parse as a dictionary (each key is a column) of lists (each element is a cell in that column)
student_data = {}
with open(args.infile) as f:
    column_headers = f.readline().strip('\n').split(',')
    lines = f.readlines()
for column in column_headers:  # adds an empty list for each column, keyed by the column name 
    student_data[column] = []
number_of_columns = len(column_headers)
for line in lines:  # appends data to the lists keyed by column names.
    row_cells = line.strip('\n').split(',')
    for index in range(0,number_of_columns):
        column_name = column_headers[index]
        cell_data = row_cells[index]
        student_data[column_name].append(cell_data)


# find most popular favorite thing for each catagory. except the first column, which are the student's names
for catagory in column_headers[1:]:
    print(catagory)
    print('Unique Favorites: ', set(student_data[catagory]))
    get_popular(student_data[catagory])