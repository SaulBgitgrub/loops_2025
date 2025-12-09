# #while loops = execute some code WHILE some condition remains true
# name = input("Enter your name: ")

# if name == "":
#     print("You did not enter your name")
# else:
#     print(f"Hello {name}")

# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name")
# print(f"Hello {name}")

# #while name == "": print("You did not enter your name")... This code is an infinite loop, and the input thing is an escape tool

# age = int(input("Enter your age: "))
# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age"))
#     print(f"You are {age} years old")

# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter a food you like (q to quit): ")

# print("bye")

# food = input("What is your favorite food")
# print()

# num = input(int("Enter a number between 1 and 10"))
# while num < 1 or num > 10:
#     print(f"{num} is not valid")
#     num = input("Enter a number between 1 and 10")

# print(f"Your number is {num}")

# # Given:
colors = ["red", "blue", "green", "yellow", "purple"]




# Challenge:
# Use a while loop to print each color UNTIL you find "yellow".
# Do NOT print "yellow" — stop before it.

index = 0
while index < len(colors):
    if colors [index] == "yellow":
        break
    print(colors[index])
    index += 1 # Increment the index to avoid infinite loop