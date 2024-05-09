import math
from typing import List

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
# sum_of_nums()

# Convert number to a reverse array of digits
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

def arr_in_reverse(num: int):
    if num < 0:
        print("number must be a positive")
        return 
    
    # res = list(map(int, str(num))[::-1])
    # res.reverse()
    # print(res)
    # return res
    
    # using list comprehension
    # to convert numbers into a list of integers
    res = [int(x) for x in str(num)]
    # using the slice notation to reverse the array
    res = res[::-1]
    print(res)
    return res

# arr_in_reverse(300)



def remove_every_other(arr):
    new_list = []
    for i in range( len(arr) ):
        if i % 2 == 0:
            new_list.append(new_list[i])
        print(arr)

my_arr = [1,2,3,4,5,6]
# remove_every_other(my_arr)

# beginner lost without a map sat Mar 30 2024
def maps(a):
    if not isinstance(a, list):
        print("please return a list")
        return []

    new_list = []
    for num in a:
        res = num * 2
        new_list.append(res)
    print(new_list)
    return new_list

# maps([0,1,2,3,4,5])



# Define a function that removes duplicates from an array of non negative 
# numbers and returns it as a result.

# The order of the sequence has to stay the same.

def distinct(seq):
    # new_seq = list(set(seq))
    # print(new_seq)
    res = []
    [res.append(x) for x in seq if x not in res]
    print(sorted(res))
    # prints [1,5,3,6] but wondering if i can also make the list in order 
    # using the sorted function "sorted()" we can organize and can specify
    # the list from ascending and decending order
    # sorted(iterable, key=key, reverse=reverse) 
    # reverse -> Optional. A Boolean. False will sort ascending, True will sort descending. Default is False
    # key -> Optional. A Function to execute to decide the order. Default is None
    

# distinct([1, 5, 3, 6, 3, 5, 6, 1])


# time complexity: O(n^2)
# space complexity: O(n)
# all we are recieving is a string of numbers

def high_and_low(numbers : str) -> str:
    # converted string into a list of characters
    # hi_and_lo = list(numbers)
    
    # Clean up the input string and split it into individual numbers
    hi_and_lo_list = numbers.split()
    # output 8 3 -5 42 -1 0 0 -9 4 7 4 -4
    # print(hi_an_lo)
    
    # we now have to append all og our duplicates in the list
    # res = []
    # for i in hi_an_lo:
    #     if i not in res:
    #         res.append(i)
    # print(res)
    
    # using a naive method by looping through the list
    # to make every number in the list into an integer
    for i in range(0, len(hi_and_lo_list)):
        hi_and_lo_list[i] = int(hi_and_lo_list[i])
    # output [1,2,3,4,5]
    
    # print(hi_and_lo)

    new_list = f"{max(hi_and_lo_list)} {min(hi_and_lo_list)}"
    print(new_list)

    return new_list



# high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")


def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        reverse_str = s[::-1]
        print (reverse_str)
        


def reverseVowels(s: str) -> str:
        s = list(s)
        
reverseVowels("hello")