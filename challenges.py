# Code for finding the longest word in a string.
def longest_word(sen):
    sen = sen.translate(None, "`~!@#$%^&*()-_=+[]{};':<>?/\|")
    arr = sen.split(" ")
    return max(arr, key=len)

print longest_word("what is the longest word here")


# Code to capitalise each letter within a string.
# Using .title changes every word in the string to a capital letter.
# Using .upper changes every LETTER in the string to be a capital letter.
def LetterCapitalize(str):
    return str.title()

print LetterCapitalize("hello world")

# Capitalizing each new word using a for loop.
def Selected_Capitals(words):
    words_new = ""
    for word in words.split(" "):
        words_new += "".join(word[0].upper() + word[1:] + " ")
    return words_new                # Note that did not have "return" within the for loop.

print Selected_Capitals("the man went to a shop")

s = "the brown fox"
s = " ".join(word[0].upper() + word[1:] for word in s.split())
print s

# Making words all caps
def uppercase(string):
    return string.upper()

print uppercase("hey man")

# Switching the cases of each letter within strings.
# There is a method in python for detecting whether a letter is lower or upper case.

def switch_case(string):
    new_string = ""
    for letter in string:
        if letter.islower():
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    return new_string

print switch_case("Should we Get a DRINK tonight?")   # Note that when used another "if" instead of "else" it gave me a different print out.

# Challenge - if a word starts with "a" the code needs to return the word "aardvark".
# If the word starts with anything else, it needs to return the word "zebra". From "clever programmer" on youtube.

def aardvark(string):
    for letter in string:       # Dont even need to have a for loop - can just start with "if" directly.
        if letter[0] == "a":
            return "aardvark"
        else:
            return "zebra"

print aardvark("anything")

# Reverse slicing

print "Hello!"[::-1]       # Go backwards for the full length of the word.
print "Hello!"[0::2]       # Start from beginning and print every second letter.
print "Hello!"[-3:]        # Prints the last 3 letters of the string. NB! Useful!
print "Hello World!"[:-3]  # Prints everything EXCEPT FOR the last 3 letters!

def reverse_slicing(string):
    return string[::-1]

print reverse_slicing("Arg")

# Gerund Slicing Challenge

def gerund_inifitive(string):
    if string[-3:] == "ing":          # Here selecting the final 3 letters of the word.
        return "to " + string[:-3]
    else:
        return "That's not a gerund!"

print gerund_inifitive("building")

# Oxford Comma challenge
# Need to return a list of at least 3 items in it where the list is displayed with commas and "and" before the last item.

def commafy(list):
    list[-1] = "and " + list[-1]      # Calling the last item in the list.
    return ", ".join(list)

print commafy(["trinket", "learning", "fun"])

new_list = ["apple", "pear", "pineapple"]
print " wtf ".join(new_list)          # Basically .join adds whatever you tell it to at the end of each item in the list.


# Number of things challenge
# Given a list of a number and a thing name make a grammatically correct sentence.

def how_many(the_list):
    if the_list[0] == 1:
        return "There is " + str(the_list[0]) + " " + the_list[1] + "."     # Python cannot concatenate/combine a string and a number/ integer! That is why the number "5" must be changed to be a string like the "There is " part!!!
    else:
        return "There are " + str(the_list[0]) + " " + the_list[1] + "s" + "."
    return the_list

print how_many([5, "trinket"])
print how_many([1, "king"])


# Abbreviator challenge (8)
# Given a string, return the string if it is less than 5 characters otherwise return 4 characters followed by a ".".

def abbreviator(string):
    if len(string) < 5:
        return string
    else:
        return string[0:4] + "."
    return string

print abbreviator("Trinket")
print abbreviator("arg")

# US States challenge (9)
# The funtion needs to lookup the state name when given its abbreviation.

#from us import states

# What the dictionary would look like if you had to do it manually instead of using the imported function:

# states = {"NY": "New York", "CA": "California", etc}

# def lookup_state(abbreviation):
#     return states[abbreviation]
#
# print lookup_state("NC")
# print lookup_state("CA")

# The us function isnt being imported.


# Morse Code challenege (10)
# Translate words into morse code.

from morse import string_to_morse
from morse import lookup

def morsify(string):
    final_string = ""
    for letter in string:
        final_string += lookup[letter]

    return final_string

print morsify("TRINKET")


# Apples and Oranges challenge (11)
# Make a function that returns "apples" if given a string, "oranges" if given an integer and "bananas" if given something else.

def fruit_labeler(thing):
    if type(thing) == str:
        return "apples"
    elif type(thing) == int:
        return "oranges"
    else:
        return "bananas"

print fruit_labeler(4)
print fruit_labeler("hello")
print fruit_labeler(4.5)