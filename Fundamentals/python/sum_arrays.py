# SUM ARRAYS (Arrays, Fundamentals)
# Write a function that takes an array of numbers and returns 
# the sum of the numbers. The numbers can be negative or 
# non-integer. If the array does not contain any numbers then 
# you should return 0.

# examples 
# input: [1, 5.2, 4, 0, -1]
# output: 9.2

# MAKE UPPERCASE (String, Fundamentals)
# Write a function which converts the input string to uppercase.

def uppercase(input_string):
    return input_string.upper()

print(uppercase("we good"))

# CALCULATE THE AVERAGE (Fundamentals, Arrays)
# Write a function which calculates the average of the numbers 
# in a given list.

# Note: Empty arrays should return 0.

def calc_avg(numbers):
    if not numbers:
        return 0

    average = sum(numbers) / len(numbers)
    return average

given_list = [1,2,3,4,5]
print(calc_avg(given_list))

# sum calculates the sum of all numbers in the list
# len gives the count of numbers in the list
