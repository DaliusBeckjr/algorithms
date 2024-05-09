snake case
l_name = ''
f_name = ''

using the ('_') this is a form of snake case that is used a lot in python

String Manipulation
using f'' (f string) we can add all the values into a single print() or return 
ex. print(f'my name is {f_name} {l_name}')

string.upper() -> returns a copy of the string with all the char in uppercase
string.lower() -> returns a copy of the string with all characters in lowercase
string.count(substring) -> returns a list of values where string is split at the given characer

string.find(substring) -> returns the index of the start of the first occurance of substring with string

string.Isalnum() -> returns boolean depending depending on whether the string length is > 0 and all characters are alphanumeric(). strings that include spaces and punctuation will return false for this method. similar method includes .isalpha(), .isdigit(), islower(), isupper(), and so on.

string.join(list) -> returns a string that is all string within our set concatenated

string.endswith() -> returns a boolean based upon whether the last characters of string match substring

List Manipulation

an array in python is called a list
some_list = [1,2,3,4,5]

.append() -> adds the element to the end of the list
.pop() -> removes and returns the last element from the list 
.reverse() -> reverses the order of elements in the list
.remove() -> searches list for the value that you want to remove
dont have a .slice()..we have [::] ->
syntax: sequence[start:stop:step]

len()


loops:
range() ->
syntax: range(start:stop:step)
ex: for i in range(0,5,1):