# Complete the function that accepts a string parameter, and 
# reverses each word in the string. All spaces in the string 
# should be retained. (Sat Jun 27 8pm)

# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"


def reverse_word(text):
    # Step 1: Split the input string into words
    # text.split(" "): This splits the input string into a list of words based on spaces.
    words = text.split(" ")
    
    # Step 2: Reverse each word using a loop
    # uses a loop to reverse each word character by character, 
    # creating a reversed word. The reversed words are then 
    # joined back into a string.
    reversed_words = []
    for word in words:
        reversed_word = ""
        for char in word:
            reversed_word = char + reversed_word
        reversed_words.append(reversed_word)
    
    # Step 3: Join the reversed words back into a string, retaining the spaces
    # " ".join(reversed_words): This joins the reversed words 
    # into a string using spaces as separators.
    reversed_text = " ".join(reversed_words)
    
    return reversed_text

print(reverse_word("This is an example!"))  # Output: "sihT si na !elpmaxe"
print(reverse_word("double  spaces"))  # Output: "elbuod  secaps"
