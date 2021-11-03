def reverse(text):      #This is code for reversing a word!
    list_number = 0     # Note how the variables are not set within the loop but outside it!
    word = ""           # Note how the variables are not set within the loop but outside it!
    for i in text:
        list_number += 1
        word += text[len(text) - list_number]
    return word

print reverse("Veliko")

#Below is code for how to remove vowels in a word or sentence, etc.
''' NB!!! Note that you can use the words "NOT IN" as part of an instruction - so just like you would use
"for i in letters_inword" you can use "for i not in letters_in word"
'''

def anti_vowel(text):
    no_vowel = ""
    for letters in text:
        if letters not in "aeiouAEIOU":   #Note the use of the 'not in'
            no_vowel += letters
    return no_vowel

print anti_vowel("I am going to the shop")

# The code below is used to replce a specific word in a sentence.

ran_word = "I went to the shop"

ran2_word = ran_word.split()               #Take note of how useful the .split function can be!

print ran2_word

a,b,c,d,e = ran_word.split()

print b        #Here I assigned the 'b' to the letter 'went' from the original string.

def censor(text, word):
    split_up = text.split()
    other_word = ""
    for data in split_up:
        if data == word:
            other_word += "*" * len(word) + " "
        else:
            other_word += data + " "
    sliced_word = other_word[:-1]
    return sliced_word

print censor("I went to the shop", "shop")

#Below is using the enumerate function.

print "\n" * 2

random_list = ['apples', 'pears', 'oranges', 'kiwis', 'apples']

for ran, value in enumerate(random_list, 1):
    print ran, value

# This is an example of counting how many times a particular item appears in a list.

def count(sequence, item):
    data_count = 0
    for info in sequence:
        if info == item:
            data_count += 1
    return data_count

print count(random_list, "apples")      # Correctly shows 2 times!

random_list.extend('bananas')
print random_list

random_list.extend(['bananas'])         #Note the difference between .extend ['bananas'] and above.

print random_list

# Below is code to find even numbers only in a list.

print "\n"

items_data = ('fruit', 'vegetables', 'meat')

def purify(list):
    x = []
    for numbers in list:
        if numbers % 2 == 0:
            x.append(numbers)
    return x

print list(items_data)        #When using the list function, the item inside () must be a tuple - i.e. cannot already be a list!

# Therefore list converts a bunch of data in a variable into a list.

# Below is code that removes duplicate values within a list.

def remove_duplicates(x):
    new_list = []
    for data in x:
        if data not in new_list:
            new_list.append(data)
    return new_list

print remove_duplicates([4,5,5,4])

# Here is the code for finding the median in a list of numbers!

def median(x):
    sorted_list = sorted(x)
    length_list = len(sorted_list)
    first_median = len(sorted_list) / 2
    second_median = first_median - 1
    for data in sorted_list:
        if length_list % 2 == 0:
            median_number = (sorted_list[first_median] + sorted_list[second_median]) / 2.0
            return median_number
        else:
            median_number = sorted_list[first_median]
            return median_number

print median([12,45,18,22,64,25])        #On line 114 I used a 2.0 to divide since I need a float/precise number!

print "\n"

# Code for calculating averages, variance and standard deviation of a list of information.

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


def grades_sum(scores):
    total = 0
    for data in scores:
        total += data
    return total


print grades_sum(grades)


def grades_average(grades):
    for data in grades:
        average_figure = grades_sum(grades) / float(len(grades))      #Used float here since need decimals also!
    return average_figure


print grades_average(grades)

# This is the variance code:

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    return (variance / len(scores))


print grades_variance(grades)

#And finally this is the standard deviation code:

def grades_std_deviation(variance):
    return variance ** 0.5


variance = grades_variance(grades)           #Creating a new variable and storing in it the result of the above function.
print grades_std_deviation(variance)

xlist = range(1,21)

print xlist.pop()                   #The pop function allows you to select only the last item

print "\n"

