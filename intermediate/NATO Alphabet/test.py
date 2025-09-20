import random
import pandas

numbers = [1,2,3]
name = 'Anant'
names = ['anant', 'manan', 'anup','dev','ishit']
# List Comprehension

new_numbers = [num+1 for num in numbers]
new_name = [letter for letter in name]
new_range = [num*2 for num in range(1,5)]
new_names = [name for name in names if len(name) <= 4]
new_names_capitals = [name.upper() for name in names]

# num+1 is new item
# num is loop variable
# numbers is the list we are working on

# print(new_numbers,new_name,new_range,new_names,new_names_capitals,sep='\n')

# Dictionary Comprehension
# {key:value for item in list}

students = {student:random.randint(1,100) for student in names}
passed_students = {student:score for (student,score) in students.items() if score > 60}
# print(students)
# print(passed_students)

student_dict = {
    "student":names,
    "score": [score for (student,score) in students.items()]
    }

data = pandas.DataFrame(student_dict)

# for (key,value) in data.items():
#     print(key,value)
for (index,row) in data.iterrows():
    # print(row)
    # print(row.student)
    print(row.score)