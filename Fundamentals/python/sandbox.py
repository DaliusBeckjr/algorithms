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