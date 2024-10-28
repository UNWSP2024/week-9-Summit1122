# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).
import random

with open("file_w_numbers.txt", "w") as f:

    how_many = random.randint(1,1000)
    for i in range(how_many):
        number = random.randint(1, 501)
        f.write(str(f"{number}\n"))

with open("file_w_numbers.txt","r") as f:
    lines = f.readlines()
    count = 0
    for i in lines:
        count = count + 1

print(f"In this mix of random numbers there were {count} numbers")