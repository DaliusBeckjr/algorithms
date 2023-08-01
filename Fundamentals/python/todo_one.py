# Print -52 to 1066

# Print integers from -52 to 1066 using a FOR loop. 

# in python we would use range() for our loops in python
# range(start, stop, step)
def loopty():
    for i in range(-52, 1067):
        print(i)
# print(loopty())

# Don’t Worry, Be Happy

# Create beCheerful(). Within it, console.log string "good morning!" Call it 98 times.

def beCheerful():
    for i in range(1,98):
        print("good morning!")
# print(beCheerful())

# Multiples of Three – but Not All

# Using FOR, print multiples of 3 from -300 to 0. Skip -3 and -6.

# explanation: By setting range(-300, 1, 3), we create a sequence that starts from -300, goes up to 0
# (exclusive), and increments by 3 at each step. The if statement inside the loop is used to skip printing -3 and -6.
# we are skipping by 3's but aren't looking through a sequence of 3

def multiples_of_three():
    for i in range (-300, 1, 3):
        if i == -3 or i == -6:
            continue
        print(i)
# print(multiples_of_three())

# Printing Integers with While

# Print integers from 2000 to 5280, using a WHILE.

# explanation: In this code, we start with num initialized to 2000, and then we use a while loop to keep
# printing num as long as it is less than or equal to 5280. After each iteration, we increment num by 1 using
# num += 1 to move to the next integer in the sequence. The loop will stop once num becomes greater than 5280.

# I had to re-teach myself how to use a while loop

# def while_int(x,y):
#     num = x

# while num <= y:
#     print(num)
#     num += 1

# print(while_int(2000, 5280))

#  ----------------------------------------

# Leap Year

# Write a function that determines whether a given year is a leap year. If a year is divisible by four, it is a leap year, unless it is divisible by 100. However, if it is divisible by 400, then it is.

# explanation: did this one in first year of college...

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Test cases
# print(is_leap_year(2000))  # True
# print(is_leap_year(2020))  # True
# print(is_leap_year(1900))  # False
# print(is_leap_year(2023))  # False

#  ------------------------------------------

# Print and Count
# Print all integer multiples of 5, from 512 to 4096. Afterward, also log how many there were.

# count = 0

# for i in range(512, 4097):
#     if i % 5 == 0:
#         print(i)
#         count += 1

# print("Total count:", count)

# Multiples of Six

# Print multiples of 6 up to 60,000, using a WHILE.

def mult_of_six():
    pass