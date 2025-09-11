"""
Meal Recommendation System

Create a program that recommends what to eat based on the time of day.
The program will:
1. Ask the user for the current time (in hours, using 24-hour format)
2. Recommend a meal or snack based on the time
3. Add a friendly message with the recommendation

"""

# Instructions for students:
# 1. Ask the user for the current time in hours (0-23)
# 2. Convert the input to an integer
# 3. Use if-elif-else to recommend different meals based on time ranges
# 4. Include a default option for unusual times


current_time = int(input("What is the current time in hours (0-23)? "))
if 0 <= current_time < 5:
    print("You should be asleep!")
elif 5 <= current_time < 10:
    print("You should have your breakfast now.")
elif 12 <= current_time < 14:
    print("You should have your lunch now.")
elif 18 <= current_time < 21:
    print("You should have your dinner now.")
elif 21 <= current_time <= 23:
    print("Maybe time for a little dessert.")
else:
    print("Grab an apple if you're peckish. You don't want to ruin your appetite before meal time!")

