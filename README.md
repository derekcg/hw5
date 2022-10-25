### ph700a-pthon-hw5
Template for github classroom for Assignment 5 of PH700A Programming for Public Health. Assignment 5 is debugging and testing.

PH700A Principles of Programming for Public Health  
Fall 2022  
Due Thursday, 10 November 2022  
 
### Assignment 5 Debugging and Testing  
 
This time the GitHub classroom for this assignment already has scripts in it, each named hw5ex1.py, hw5ex2.py, etc. Your task in this assignment will be to test and debug these scripts. This document will tell you the intended function of each script. The main deliverable will be the fixed version of these scripts. Be sure to add, commit, and push your changes to these existing scripts. 

For Exercises 4 and 5, there is an additional deliverable. The scripts hw5ex4.py and hw5ex5.py will run without error on the provided input files, but they do not give the intended output for all cases. Create your own test input files to probe what corner cases cause the scripts to give unintended output. Then debug the scripts so that they will run correctly on your test input files. The deliverables for Exercise 4 and 5 are both the fixed scripts and your test input files. Use this address to access assignment 5: 

**Exercise 1**  
The script hw5ex1.py is intended to read a csv file with students’ scores (student_scores.csv), and then write a new csv file with the students’ letter grades (student_letters.csv). 
 

**Exercise 2**  
The script hw5ex2.py is intended to read a tab separated file with students’ favorite flowers (flowers.txt), then prompts the user to enter the name of a student. The script is intended to print the favorite flower of the named student, and print “student not found” if the name given by the user doesn’t match a student in flowers.txt.

**Exercise 3**  
The script hw5ex3.py is intended to read a csv file with students’ favorite flowers, fruit, and colors (student_favorites.csv). It then prompts the user for a color, and then prints the name of each student whose favorite color matches the user’s choice. If no students have that favorite color, then the program will instead say the choice was unique. It then does the same for fruit and flower. 

**Exercise 4**  
The script hw5ex4.py is also intended to read a csv file with students’ favorite flowers, fruit, and colors. By default, it reads student_favorites.csv, but if the user runs the code with the option -i, the user can specify the input file. For example, to have the script read a test input file named test_favorites.csv, the user could run the script like this python hw5ex4.py -i test_favorites.csv. For each category (Flowers, Fruit, and Colors), the script prints all unique favorites and prints the most popular favorite. In the case of a tie, both of the tying most popular favorites should be printed. Create a test input file called test_favorites.csv that you can use to test whether hw5ex4.py truly has the intended functionality. If it does not, debug it so that it does. Your deliverables are both the fixed hw5ex4.py and your test_favorites.csv. 
 
**Exercise 5**  
The script hw5ex5.py is intended to read a csv file with patient test results and demographics. By default it will read binary_patent_data.csv, but the user can specify the name of the input file with the -i option. For example, to have the script read a test input file named test_patients.csv, the user could run the script like this python hw5ex5.py -i test_patients.csv. The script is intended to measure the strength of any association between old age (age >= 65) and a positive test result, stratifying by gender. The script should print two odds ratios, one for males and one for females. The script should also exclude patients under 16. Create a test input file called test_patients.csv that you can use to test whether hw5ex5.py truly has the intended functionality. If it does not, debug it so that it does. Your deliverables are both the fixed hw5ex5.py and your test_patients.csv.
