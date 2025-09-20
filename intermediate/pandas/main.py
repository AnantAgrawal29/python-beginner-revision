import pandas
# import csv

# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# with open("my_file.txt", mode='a') as file:
#     file.write("\nHi, How are you?")

# with open("my_file.txt", mode='r') as file:
#     contents = file.read()
#     print(contents)

# with open("new.txt", mode='a') as file:
#     file.write("\nHi, How are you?")

# with open("new.txt", mode='r') as file:
#     contents = file.read()
#     print(contents)


# with open("weather_data.csv", 'r') as file:
#     data = (file.read()).split('\n')[1:]
# print(data)


# with open("weather_data.csv", 'r') as file:
#     data = csv.reader(file)
#     temp = []
#     for row in data:
#         if row[1]!="temp":
#             temp.append(int(row[1]))
#     print(temp)

data = pandas.read_csv("weather_data.csv")

# print(type(data)) # Dataframe
# print(data['temp'])

data_dict  = data.to_dict()
temp = data['temp'].to_list()

# data.day = data['day']

# avgTemp = sum(temp) // len(temp)
# print(avgTemp)
# print(data['temp'].mean())
# print(data['temp'].max())

monday = data[data['day'] == 'Monday']
monday_temp = monday.temp*(9 / 5) + 32
# print(monday_temp)
# print(data[data['temp'] == data['temp'].max()])

# Creating a DataFrame

data_dict = {
    "students": ["Anant","Manan","Anshika"],
    "scores": [30,40,50]
}

data = pandas.DataFrame(data_dict)
# print(data)
data.to_csv("new-data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colors = data['Primary Fur Color']
gray = len(data[colors == 'Gray'])
red = len(data[colors == 'Cinnamon'])
black = len(data[colors == 'Black'])

data_dict = {
    "Fur Color": ['gray','red', 'black'],
    "Count": [gray,red,black]
}

data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_count.csv")
