# The Importance of Functions

note that I have created two files in this folder. One uses functions, the other does not.

Here are some reasons why the function app is decisively better: 

### WithOUT functions you get this:
* 140 lines of repetitive code!!
* Same validation logic copied 9 times
* Same grade calculation logic copied 3 times
* Hard to find bugs (need to fix in multiple places)
* Difficult to modify (want to add Test 4? Change 3+ places)
* No way to test individual parts

### With functions you get this:
* 96-ish lines - almost cut in half! This is great!!!
* Each piece of logic written once
* Easy to test individual functions (Will teach this in detail later in course)
* Easy to modify (change get_valid_score() once, affects everything)
* Much more readable and organized
* Can easily add more students with a simple loop