#!/usr/bin/python3

heroes= ["Spiderman", "Batman", "Black Panther", "Wonder Woman", "Storm"]

# PART 1
# Print out your favorite character from this list! The output would look something like:
# My favorite character is Black Panther!
print(heroes[1])


# PART 2
# Ask the user to pick a number between 1 and 100.
# Convert the input into an integer.
pick_num = input("Pick a number between 1 and 100: ")

num_choice = int(pick_num)
print(num_choice)

print("The number you picked was: " + pick_num)


nums= [1, -5, 56, 987, 0]

# PART 3
# check out https://docs.python.org/3/library/functions.html or go to Google
# use a built-in function to find which integer in nums is the biggest.
# then, print out that number!
max_num = max(nums)

print("The biggest number is: " + str(max_num))
