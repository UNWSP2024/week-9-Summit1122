# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.  

# The program should handle the following exceptions: 

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file 
# are converted to a number.
def sum_numbers_from_file():
    ######################
    # Add your code here #
    try:
        with open("numbers.txt","r") as f:
            sum = 0
            for n in f:
                n = n.strip()
                sum = sum + int(n)

    except IOError:
        print("An error occurred trying to read the file.")
    except ValueError:
        print("Non_numeric date found in file")





    ######################
    print('In the sum_numbers_from_file function')
    print(f"The total value of all the numbers in the file is {sum}")
# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()