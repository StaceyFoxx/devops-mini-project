"""
Weather Activity Recommender

Create a program that:
1. Asks the user for today's weather (sunny, rainy, or snowy)
2. Uses if-else to recommend an appropriate activity
3. Tells the user to have a great day

"""

# Instructions for students:
# 1. Ask the user for the current weather
# 2. Based on their input, recommend a suitable activity
# 3. Handle invalid inputs with a default message

weather = input("Is the weather sunny, rainy, or snowy? ")

if weather.lower() == "sunny":
    print("Go to the beach.")
elif weather.lower() == "rainy":
    print("Read a book.")
elif weather.lower() == "snowy":
    print("Go skiing.")
else:
    print("Have a great day")
