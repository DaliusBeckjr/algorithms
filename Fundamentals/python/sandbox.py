import math

# complete the solution so that it reverses the string passed into it. 
# example 'world' -> 'dlrow'

def solution(str):
    # str = ""

    reverse_str = str[::-1]
    print(reverse_str)
    return reverse_str

# solution('world')

# another solution
# def solution(string):
#     # Pythonic way :)
#     return string[::-1]

#     # For beginners it's good practise 
#     # to know how reverse() or [::-1]
#     # works on the surface
#     #for char in range(len(string)-1,-1,-1):
#         #return string[char]

# to use pythons reverse method we need to convert the string into a list first
def backwards(str):
    # to make a list we use the 'list' built in function
    # convert the string into a list of characters
    str_list = list(str)
    # reverse the list of characters in place
    str_list.reverse()
    # converts the list of characters back into a string
    reverse_str = ''.join(str_list)
    print (reverse_str)
    return reverse_str

# backwards('done')

def str_to_arr(str):
    # if str.strip():
    #     phrase_list = str.split()
    # else:
    #     phrase_list = ['']
    # print(phrase_list)
    # return phrase_list
    return str.split() or ['']

# str_to_arr("hello world")
# print(str_to_arr("hello world"))
# str_to_arr(" ")
# print( str_to_arr(" "))

# def square_sum(n):
#     arr = n
#     sum = 0

#     for i in range(0, len(arr)):
#         sum = sum + arr[i]**2
#         print(sum)
#         return sum

# square_sum([1,5,6])
def square_sum(numbers):
    if not isinstance(n, list):
        print("Input is not a list")
        return
    
    arr = n
    total_sum = 0

    for num in arr:
        squared_num = num ** 2
        total_sum += squared_num
    
    print(total_sum)
    # sum = 0
    # for n in numbers:
    #     sum = sum + n*n
    #     print(sum)
    # return sum

# square_sum([1, 5, 6])

some_list = [1,2,3,4,5]

# for i in range():
#     print(some_list[i])

is_instructor = False

# if is_instructor:
#     print("yessirrr")
# else:
#     print("no sirrrski")

def fizz_buzz():
    for i in range(1, 101):
        
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# print(fizz_buzz())

# def starterkit(n: int):
#     print(f"I am only {n}")

# starterkit(5)

def make_negative(number: int):
    print(number)
    return number if number <= 0 else number * -1

# other answer
    # if number <= 0:
    #     print(number)
    #     return number
    # else:
    #     number = number * -1
    #     print(number)
    #     return number

# make_negative(5)
# make_negative(0)
# make_negative(-4)

def one_to_two_fifty_five():
    # print 1 - 255
    for i in range(1, 256, 1):
        print(i)

# print(one_to_two_fifty_five())

def odd_num():
    for i in range(1,255,2):
        print(i)

# print(odd_num())

def sum_of_nums():
    total_sum = 0  # Initialize the sum variable to 0
    for i in range(1, 256, 1):  # Iterate from 1 to 255 (inclusive)
        total_sum += i  # Add the current value of 'i' to the sum
    print(total_sum)  # Print the final sum

# Call the function to calculate and print the sum
sum_of_nums()