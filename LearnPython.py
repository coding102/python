# %%
# Print String 5 times
import datetime
import random
from audioop import mul
from itertools import count


for i in range(5):
    print("This is fun")


# %%
# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)


# %%
# Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)


# %%
# Print all items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])


# %%
# Print all items, using a while loop to go through all the index numbers
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1


# %%
def area_triangle(base, height):
    return base*height/2


area_a = area_triangle(5, 4)
area_b = area_triangle(7, 3)
sum = area_a + area_b
print("The sum of both areas is: " + str(sum))


# %%
def get_seconds(hours, minutes, seconds):
    return 3600*hours + 60*minutes + seconds


amount_a = get_seconds(2, 30, 0)
amount_b = get_seconds(0, 45, 15)
result = amount_a + amount_b
print(result)


# %%
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)


# %%

# name = "Kay"
# number = len(name) * 9
# print("Hello " + name + " . Your lucky number is " + str(number))

# name = "Cameron"
# number = len(name) * 9
# print("Hello " + name + " . Your lucky number is " + str(number))


def lucky_number(name):
    number = len(name) * 9
    print("Hello " + name + " . Your lucky number is " + str(number))


lucky_number("Kay")
lucky_number("Mark")

# %%
# REPLACE THIS STARTER CODE WITH YOUR FUNCTION
# june_days = 30
# print("June has " + str(june_days) + " days.")
# july_days = 31
# print("July has " + str(july_days) + " days.")


def month_days(month, days):
    print(month + " has " + str(days) + " days.")


month_days("june", 30)
month_days("july", 31)


# %%
def rectangle_area(base, height):
    area = base*height
    print("The area is " + str(area))


rectangle_area(5, 6)

# %%
# branching

# if condition1:
# if-block
# elif condition2:
# elif-block
# else:
# else-block


# %%
# This function compares two numbers and returns them in increasing order.
def order_numbers(number1, number2):
    if number2 > number1:
        return number1, number2
    else:
        return number2, number1


# 1) Fill in the blanks so the print statement displays the result of the function call
smaller, bigger = order_numbers(5, 100)
print(smaller, bigger)


# %%
def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters long")
    else:
        print("Valid username")


# %%
def number_group(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return"Zero"


print(number_group(10))  # Should be Positive
print(number_group(0))  # Should be Zero
print(number_group(-5))  # Should be Negative


# %%
# If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one byte will still use 4096 bytes of
# storage. A file made up of 4097 bytes will use 4096*2=8192 bytes of storage. Knowing this, can you fill in the gaps in the
# calculate_storage function below, which calculates the total number of bytes needed to store a file of a given size?


def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return 4096 * (full_blocks + 1)
    return 4096


print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096))  # Should be 4096
print(calculate_storage(4097))  # Should be 8192
print(calculate_storage(6000))  # Should be 8192


# %%
x = 0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x + 1
print("x=" + str(x))


# %%
def print_range(start, end):
    # Loop through the numbers from start to end
    n = start
    while n < end:
        n = n + 1
        print(n)


print_range(0, 5)  # Should print 1 2 3 4 5 (each number on its own line)


# Make the print_prime_factors function print all the prime factors of
# a number. A prime factor is a number that is prime and divides another without a remainder.
# %%
def print_prime_factors(number):
    # Start with two, which is the first prime
    factor = 2
    # Keep going until the factor is larger than the number
    while factor <= number:
        # Check if factor is a divisor of number
        if number % factor == 0:
            # If it is, print it and divide the original number
            print(factor)
            number = number / factor
        else:
            # If it's not, increment the factor by one
            factor += 1
    return "Done"


print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT


# Write a function so that it returns the sum of all
# the divisors of a number, without including it. A divisor is a number that divides into another without a remainder.
# %%
def sum_divisors(n):
    sum = 0
    i = 1
    # Return the sum of all divisors of n, not including n
    while i < n:
        if n % i == 0:
            sum += i
            i += 1
        else:
            i += 1
    return sum


print(sum_divisors(0))
# 0
print(sum_divisors(3))  # Should sum of 1
# 1
print(sum_divisors(36))  # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102))  # Should be sum of 2+3+6+17+34+51
# 114


# The multiplication_table function prints the results of a number passed to it multiplied by 1 through 5.
# An additional requirement is that the result is not to exceed 25, which is done with the break statement.
# %%
def multiplication_table(number):
    # Initialize the starting point of the multiplication table
    multiplier = 1
    # Only want to loop through 5
    while multiplier <= 5:
        result = number * multiplier
        # What is the additional condition to exit out of the loop?
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        # Increment the variable for the loop
        multiplier += 1


multiplication_table(3)
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5)
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)
# Should print: 8x1=8 8x2=16 8x3=24


# Fill in the gaps of the sum_squares function, so that it returns the sum of all the squares of numbers between
# 0 and x (not included). Remember that you can use the range(x) function to generate a sequence of numbers
# from 0 to x (not included).
# %%
def square(n):
    return n*n


def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum


print(sum_squares(10))  # Should be 285


# calculate total sum and average
# %%
values = [23, 52, 59, 37, 48]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1
print("Total sum: " + str(sum) + " - Average: " + str(sum/length))


# In math, the factorial of a number is defined as the product of an integer and all the integers below it.
# For example, the factorial of four (4!) is equal to 1*2*3*4=24. Fill in the blanks to make the factorial
# function return the right number.
# %%
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result


print(factorial(4))  # should return 24
print(factorial(5))  # should return 120


# The function sum_positive_numbers should return the sum of all positive numbers between the number n received
# and 1. For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15. Fill
# in the gaps to make this work:
# %%
# using recursion
def sum_positive_numbers(n):
    if n <= 1:
        return n
    return n + sum_positive_numbers(n-1)


print(sum_positive_numbers(3))  # Should be 6
print(sum_positive_numbers(5))  # Should be 15


# using normal functions
def sum_positive_numbers(n):
    sums = 0
    for v in range(1, n+1):
        sums += v
    return sums


print(sum_positive_numbers(3))  # Should be 6
print(sum_positive_numbers(5))  # Should be 15


# Modify the double_word function so that it returns the same word repeated twice, followed by the length of
# the new doubled word. For example, double_word("hello") should return hellohello10.
# %%
def double_word(word):
    return word * 2 + str(len(word * 2))


print(double_word("hello"))  # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0


# Want to give it a go yourself? Be my guest! Modify the first_and_last function so that it returns True
# if the first letter of the string is the same as the last letter of the string, False if they???re different.
# Remember that you can access characters using message[0] or message[-1].
# Be careful how you handle the empty string, which should return True since nothing is equal to nothing.
# %%
def first_and_last(message):
    if len(message) == 0:
        return True
    elif message[0] == message[-1]:
        return True
    else:
        return False


print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))


# Write a program "function" that replaces an old domain with the new one in any outdated email addresses
# %%
# 3 parameters: email address to be checked, old domain, and new domain
def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:  # check if the concat of the @ and old domain are in the email address using "in"
        # find index where old domain (including @ sign) starts
        index = email.index("@" + old_domain)
        # use the index to create the new email
        new_email = email[:index] + "@" + new_domain
        return new_email  # return new email
    return email  # if the email didn't contain new domain just return it


# Fill in the gaps in the initials function so that it returns the initials of the words contained
# in the phrase received, in upper case. For example: "Universal Serial Bus" should return "USB"; "local area network"
# should return "LAN???.
# %%
def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result


print(initials("Universal Serial Bus"))  # Should be: USB
print(initials("local area network"))  # Should be: LAN
print(initials("Operating system"))  # Should be: OS


# %%
name = "Mark"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))
print("Your lucky number is {number}, {name}.".format(
    name=name, number=len(name)*3))


# Modify the student_grade function using the format method, so that it returns the phrase "X received Y% on the exam". For example,
# student_grade("Reed", 80) should return "Reed received 80% on the exam".
# %%
def student_grade(name, grade):
    return "{name} received {grade}% on the exam".format(name=name, grade=grade)


print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))


# %%
price = 7.5
with_tax = price * 1.09
print(price, with_tax)

print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))


# %%
def to_celsius(x):
    return (x-32)*5/9


for x in range(0, 101, 10):
    # align to right 3 spaces, 2 decimal places and align to the right 6 spaces
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))


# The is_palindrome function checks if a string is a palindrome. A palindrome is a string that can be equally read from left to right or
# right to left, omitting blank spaces, and ignoring capitalization. Examples of palindromes are words like kayak and radar, and phrases
#  like "Never Odd or Even". Fill in the blanks in this function to return True if the passed string is a palindrome, False if not.
# %%
def is_palindrome(input_string):
    # We'll create two strings, to compare them
    new_string = ""
    reverse_string = ""
    # Traverse through each letter of the input string
    for string in input_string.lower():
        # Add any non-blank letters to the
        # end of one string, and to the front
        # of the other string.
        if string.replace(" ", ""):
            new_string = new_string + string
            reverse_string = string + reverse_string
    # Compare the strings
    if reverse_string == new_string:
        return True
    return False


print(is_palindrome("Never Odd or Even"))  # Should be True
print(is_palindrome("abc"))  # Should be False
print(is_palindrome("kayak"))  # Should be True


# Using the format method, fill in the gaps in the convert_distance function so that it returns the phrase "X miles equals Y km", with Y having
# only 1 decimal place. For example, convert_distance(12) should return "12 miles equals 19.2 km".
# %%
def convert_distance(miles):
    km = miles * 1.6
    result = "{} miles equals {:.1f} km".format(miles, km)
    return result


print(convert_distance(12))  # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5))  # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11))  # Should be: 11 miles equals 17.6 km


# Fill in the gaps in the nametag function so that it uses the format method to return first_name and the first initial of last_name followed by a period.
# For example, nametag("Jane", "Smith") should return "Jane S."
# %%
def nametag(first_name, last_name):
    return("{} {}.".format(first_name, last_name[0]))


print(nametag("Jane", "Smith"))
# Should display "Jane S."
print(nametag("Francesco", "Rinaldi"))
# Should display "Francesco R."
print(nametag("Jean-Luc", "Grand-Pierre"))
# Should display "Jean-Luc G."


# The replace_ending function replaces the old string in a sentence with the new string, but only if the sentence ends with the old string. If there
# is more than one occurrence of the old string in the sentence, only the one at the end is replaced, not all of them. For example,
# replace_ending("abcabc", "abc", "xyz") should return abcxyz, not xyzxyz or xyzabc. The string comparison is case-sensitive,
# so replace_ending("abcabc", "ABC", "xyz") should return abcabc (no changes made).
# %%
def replace_ending(sentence, old, new):
    # Check if the old string is at the end of the sentence
    if sentence.endswith(old):
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the
        # end with the new string
        i = sentence.rindex(old)
        new_sentence = sentence[:i]+new
        return new_sentence

    # Return the original sentence if there is no match
    return sentence


print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april"))
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April"))
# Should display "The weather is nice in April"


# Using the "split" string method from the preceding lesson, complete the get_word function to return the {n}th word from a passed sentence. For example,
# get_word("This is a lesson about lists", 4) should return "lesson", which is the 4th word in this sentence. Hint: remember that list indexes start at 0, not 1.
# %%
def get_word(sentence, n):
    # Only proceed if n is positive
    if n > 0:
        words = sentence.split()
        # Only proceed if n is not more than the number of words
        if n <= len(words):
            return(words[n-1])
    return("")


print(get_word("This is a lesson about lists", 4))  # Should print: lesson
print(get_word("This is a lesson about lists", -4))  # Nothing
print(get_word("Now we are cooking!", 1))  # Should print: Now
print(get_word("Now we are cooking!", 5))  # Nothing


# The skip_elements function returns a list containing every other element from an input list, starting with the first element. Complete this function to do that,
# using the for loop to iterate through the input list.
# %%
def skip_elements(elements):
    # Initialize variables
    new_list = []
    i = 0

    # Iterate through the list
    for element in elements:
        # Does this element belong in the resulting list?
        if i % 2 == 0:
            # Add this element to the resulting list
            new_list.append(element)
        # Increment i
        i += 1

    return new_list


# Should be ['a', 'c', 'e', 'g']
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))
# Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))
print(skip_elements([]))  # Should be []


# Let's use tuples to store information about a file: its name, its type and its size in bytes. Fill in the gaps in this code to return the size in kilobytes
# (a kilobyte is 1024 bytes) up to 2 decimal places.
# %%
def file_size(file_info):
    name, tpe, size = file_info
    return("{:.2f}".format(size / 1024))


print(file_size(('Class Assignment', 'docx', 17875)))  # Should print 17.46
print(file_size(('Notes', 'txt', 496)))  # Should print 0.48
print(file_size(('Program', 'py', 1239)))  # Should print 1.21


# %%
# iterate over list of strings
animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
characters = 0
for animal in animals:  # for each string
    # get length and add it to the total amount of characters
    characters += len(animal)

# print total and average by dividing total by the length of the list
print("Total characters: {}, Average length: {}".format(
    characters, characters/len(animals)))


# Try out the enumerate function for yourself in this quick exercise. Complete the skip_elements function to return every other element from the list, this time
# using the enumerate function to check if an element is on an even position or an odd position.
# %%
def skip_elements(elements):
    # code goes here
    other_list = []
    for index, word in enumerate(elements):
        if index % 2 == 0:
            other_list.append(word)
    return other_list


# Should be ['a', 'c', 'e', 'g']
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))
# Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))


# write a function that creates a new list containing one string per person including name and email address example: Mark Smith <mark@example.com>
# %%
def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result


print(full_emails([("alex@example.com", "Alex Smith")]))


# %%

multiples = []
for x in range(1, 11):
    multiples.append(x*7)
print(multiples)

# use list comprehension to accomplish the same task as above
# %%
multiples = [x*7 for x in range(1, 11)]
print(multiples)


# list of strings - generate list of lengths of strings
# %%
languages = ["Python", "Ruby", "Java", "Go"]
lengths = [len(language) for language in languages]

print(lengths)


# print all numbers divisible by 3 between 0 and 100
# %%
z = [x for x in range(0, 101) if x % 3 == 0]
print(z)


# The odd_numbers function returns a list of odd numbers between 1 and n, inclusively. Fill in the blanks in the function, using
# list comprehension. Hint: remember that list and range counters start at 0 and end at the limit minus 1.
# %%
def odd_numbers(n):
    return [x for x in range(0, n+1) if x % 2 != 0]


print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10))  # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11))  # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1))  # Should print []


# Given a list of filenames, we want to rename all the files with extension hpp to the extension h. To do this, we would like to generate
# a new list called newfilenames, consisting of the new filenames. Fill in the blanks in the code using any of the methods you???ve learned
# thus far, like a for loop or a list comprehension.
# %%
filenames = ["program.c", "stdio.hpp",
             "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = [filename.replace(".hpp", ".h") for filename in filenames]

print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


# Let's create a function that turns text into pig latin: a simple text transformation that modifies each word moving the first character to
# the end and appending "ay" to the end. For example, python ends up as ythonpay.
# %%
def pig_latin(text):
    say = ""
    # Separate the text into words
    words = text.split()
    for word in words:
        # Create the pig latin word and add it to the list
        texts = word[1:] + word[0] + "ay" + " "
        say += texts
        # Turn the list back into a phrase
    return say


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
# Should be "rogrammingpay niay ythonpay siay unfay"
print(pig_latin("programming in python is fun"))


# The permissions of a file in a Linux system are split into three sets of three permissions: read, write, and execute for the owner, group,
# and others. Each of the three values can be expressed as an octal number summing each permission, with 4 corresponding to read, 2 to write, and 1
# to execute. Or it can be written with a string using the letters r, w, and x or - when the permission is not granted.
# For example:
# 640 is read/write for the owner, read for the group, and no permissions for the others; converted to a string, it would be: "rw-r-----"
# 755 is read/write/execute for the owner, and read/execute for group and others; converted to a string, it would be: "rwxr-xr-x"
# Fill in the blanks to make the code convert a permission in octal format into a string format.
# %%
def octal_to_string(octal):
    result = ""
    value_letters = [(4, "r"), (2, "w"), (1, "x")]
    # Iterate over each of the digits in octal
    for digit in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if digit >= value:
                result += letter
                digit -= value
            else:
                result += "-"
    return result


print(octal_to_string(755))  # Should be rwxr-xr-x
print(octal_to_string(644))  # Should be rw-r--r--
print(octal_to_string(750))  # Should be rwxr-x---
print(octal_to_string(600))  # Should be rw-------


# The group_list function accepts a group name and a list of members, and returns a string with the format: group_name: member1, member2, ??? For example,
# group_list("g", ["a","b","c"]) returns "g: a, b, c". Fill in the gaps in this function to do that.
# %%
def group_list(group, users):
    members = ', '.join(users)
    return '{}: {}'.format(group, members)


# Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"]))
# Should be "Engineering: Kim, Jay, Tom"
print(group_list("Engineering", ["Kim", "Jay", "Tom"]))
print(group_list("Users", ""))  # Should be "Users:"


# The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, and prints the sentence
# "Guest is X years old and works as __." for each one. For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer"))
# should print out: Ken is 30 years old and works as Chef. Pat is 35 years old and works as Lawyer. Amanda is 25 years old and works as Engineer.
# Fill in the gaps in this function to do that.
# %%
def guest_list(guests):
    for guest in guests:
        name, age, job = guest
        print("{} is {} years old and works as {}".format(name, age, job))


guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'),
           ('Amanda', 25, "Engineer")])

# Click Run to submit code
# Output should match:
# Ken is 30 years old and works as Chef
# Pat is 35 years old and works as Lawyer
# Amanda is 25 years old and works as Engineer


# Dictionary
# %%
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
print(file_counts)

file_counts["txt"]  # count how many txt files
"jpeg" in file_counts  # does the file jpg exist?
# add file type and count, if file type already exist count is replaced
file_counts["pdf"] = 10
print(file_counts)
del file_counts["pdf"]  # delete file type
print(file_counts)


# The "toc" dictionary represents the table of contents for a book. Fill in the blanks to do the following: 	1) Add an entry for Epilogue on page 39.
# 2) Change the page number for Chapter 3 to 24.
# 3) Display the new dictionary contents.
# 4) Display True if there is Chapter 5, False if there isn't.
# %%
toc = {"Introduction": 1, "Chapter 1": 4,
       "Chapter 2": 11, "Chapter 3": 25, "Chapter 4": 30}
toc["Epilogue"] = 39  # Epilogue starts on page 39
toc["Chapter 3"] = 24  # Chapter 3 now starts on page 24
print(toc)  # What are the current contents of the dictionary?
print("Chapter 5" in toc)  # Is there a Chapter 5?


# ITERATING over dictionary content
# %%
file_counts = {"jpeg": 10, "txt": 20, "csv": 30, "py": 15}
for extension in file_counts:
    print(extension)  # will only print key


for ext, amount in file_counts.items():  # print key and value pair using the items() method, it will return a tuple for each element in the dictionary
    print("There are {} files with the .{} extension".format(amount, ext))


file_counts.keys()  # return keys
file_counts.values()  # return values

# Use items() to get both key and value
# Use keys() to get keys
# Use values() to get values

for value in file_counts.values():
    print(value)


# Complete the code to iterate through the keys and values of the cool_beasts dictionary. Remember that the items method returns a tuple of key, value for each
# element in the dictionary.
# %%
cool_beasts = {"octopuses": "tentacles", "dolphins": "fins", "rhinos": "horns"}
for animals, features in cool_beasts.items():
    print("{} have {}".format(animals, features))


# How times do letters appear in a piece of text?
# %%
def count_letters(text):
    result = {}  # initialize an empty dictionary
    for letter in text:  # go through each letter in the given string
        if letter not in result:  # for each letter check if it's already in the given string
            result[letter] = 0  # if not in dictionary add it
        # increment the count for that letter in the dictionary
        result[letter] += 1
    return result


count_letters("MarkM")


# In Python, a dictionary can only hold a single value for a given key. To workaround this, our single value can be a list containing multiple values. Here we have
# a dictionary called "wardrobe" with items of clothing and their colors. Fill in the blanks to print a line for each item of clothing with each color, for example:
# "red shirt", "blue shirt", and so on.
# %%
wardrobe = {"shirt": ["red", "blue", "white"], "jeans": ["blue", "black"]}
for key, value in wardrobe.items():
    for i in value:
        print("{} {}".format(i, key))


# The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values. Fill in the blanks to generate a list that contains
# complete email addresses (e.g. diana.prince@gmail.com).
# %%
def email_list(domains):
    emails = []
    for domain, users in domains.items():
        for user in users:
            emails.append(user+'@'+domain)
        return(emails)


print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": [
      "barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))


# The groups_per_user function receives a dictionary, which contains group names with the list of users. Users can belong to multiple groups. Fill in the blanks to return a
# dictionary with the users as keys and a list of their groups as values.
# %%
def groups_per_user(group_dictionary):
    user_groups = {}
    for group, users in group_dictionary.items():
        for user in users:
            if user not in user_groups:
                user_groups[user] = []
            user_groups[user].append(group)
    return user_groups


print(groups_per_user({"local": ["admin", "userA"],
                       "public":  ["admin", "userB"],
                       "administrator": ["admin"]}))


# *********************************************************************************************
# The add_prices function returns the total price of all of the groceries in the  dictionary. Fill in the blanks to complete this function.
# %%

def add_prices(basket):
    # Initialize the variable that will be used for the calculation
    total = 0
    # Iterate through the dictionary items
    for items, price in basket.items():
        # Add each price to the total calculation
        # Hint: how do you access the values of
        # dictionary items?
        total += price
    # Limit the return value to 2 decimal places
    return round(total, 2)


groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
             "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries))  # Should print 28.44

# ***********************************************************************************************


# The format_address function separates out parts of the address string into new strings: house_number and street_name, and returns: "house number X on street named Y".
# The format of the input string is: numeric house number, followed by the street name which may contain numbers, but never by themselves, and could be several words
# long. For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive". Fill in the gaps to complete this function.
# %%
def format_address(address_string):
    # Declare variables
    streetNumber = ""
    streetName = ""

    # Separate the address string into parts
    address_string = address_string.split()

    # Traverse through the address parts
    for i in address_string:
        # Determine if the address part is the
        # house number or part of the street name
        if i.isdigit():
            streetNumber = i
        else:
            streetName += i
            streetName += ''
    # Does anything else need to be done
    # before returning the result?

    # Return the formatted string
    return "house number {} on street named {}".format(streetNumber, streetName)


print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"


# The highlight_word function changes the given word in a sentence to its upper-case version. For example, highlight_word("Have a nice day", "nice")
# returns "Have a NICE day". Can you write this function in just one line?
# %%
def highlight_word(sentence, word):
    return(sentence.replace(word, word.upper()))


print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))


# A professor with two assistants, Jamie and Drew, wants an attendance list of the students, in the order that they arrived in the classroom. Drew was the
# first one to note which students arrived, and then Jamie took over. After the class, they each entered their lists into the computer and emailed them to
# the professor, who needs to combine them into one, in the order of each student's arrival. Jamie emailed a follow-up, saying that her list is in reverse
# order. Complete the steps to combine them into one list as follows: the contents of Drew's list, followed by Jamie's list in reverse order, to get an
# accurate list of the students as they arrived.
# %%
def combine_lists(list1, list2):

    # Generate a new list containing the elements of list2
    new_list = list2
# Followed by the elements of list1 in reverse order
    for i in reversed(range(len(list1))):
        new_list.append(list1[i])
    return new_list


Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))


# Use a list comprehension to create a list of squared numbers (n*n). The function receives the variables start and end, and returns a list of squares of
# consecutive numbers between start and end inclusively.
# For example, squares(2, 3) should return [4, 9].
# %%
def squares(start, end):
    return [n*n for n in range(start, end+1)]


print(squares(2, 3))  # Should be [4, 9]
print(squares(1, 5))  # Should be [1, 4, 9, 16, 25]
print(squares(0, 10))  # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# Complete the code to iterate through the keys and values of the car_prices dictionary, printing out some information about each one.
# %%
def car_listing(car_prices):
    result = ""
    for cars in car_prices:
        result += "{} costs {} dollars".format(cars, car_prices[cars]) + "\n"
    return result


print(car_listing({"Kia Soul": 19000, "Lamborghini Diablo": 55000,
      "Ford Fiesta": 13000, "Toyota Prius": 24000}))


# Taylor and Rory are hosting a party. They sent out invitations, and each one collected responses into dictionaries, with names of their friends and how many
# guests each friend is bringing. Each dictionary is a partial list, but Rory's list has more current information about the number of guests. Fill in the blanks
# to combine both dictionaries into one, with each friend listed only once, and the number of guests from Rory's dictionary taking precedence, if a name is
# included in both dictionaries. Then print the resulting dictionary.
# %%
def combine_guests(guests1, guests2):
    # Combine both dictionaries into one, with each key listed
    guests2.update(guests1)
    # only once, and the value from guests1 taking precedence
    return guests2


Rorys_guests = {"Adam": 2, "Brenda": 3, "David": 1,
                "Jose": 3, "Charlotte": 2, "Terry": 1, "Robert": 4}
Taylors_guests = {"David": 4, "Nancy": 1,
                  "Robert": 2, "Adam": 1, "Samantha": 3, "Chris": 5}

print(combine_guests(Rorys_guests, Taylors_guests))


# Use a dictionary to count the frequency of letters in the input string. Only letters should be counted, not blank spaces, numbers, or punctuation.
# Upper case should be considered the same as lower case. For example, count_letters("This is a sentence.")
# should return {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.
# %%
def count_letters(text):
    result = {}
    text = text.lower()
    # Go through each letter in the text
    for letter in text:
        # Check if the letter needs to be counted or not
        if letter.isalpha() and letter not in result:
            # Add or increment the value in the dictionary
            result[letter] = text.lower().count(letter)
    return result


print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}


# What do the following commands return when animal = "Hippopotamus"?
# %%
animal = "Hippopotamus"

print(animal[3:6])
print(animal[-5])
print(animal[10:])


# What does the list "colors" contain after these commands are executed?
# %%
colors = ["red", "white", "blue"]
colors.insert(2, "yellow")
print(colors)


# What do the following commands return?
# %%
host_addresses = {"router": "192.168.1.1",
                  "localhost": "127.0.0.1", "google": "8.8.8.8"}
host_addresses.keys()
print(host_addresses)


# Instance Methods
# %%
class Piglet:
    name = "piglet"

    def speak(self):
        print("Oink! I'm {}! Oink!".format(self.name))


hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()


# Have a go at writing methods for a class.
# Create a Dog class with dog_years based on the Piglet class shown before (one human year is about 7 dog years).
# %%
class Dog:
    years = 0

    def dog_years(self):
        return self.years * 7


fido = Dog()
fido.years = 3
print(fido.dog_years())


# What Is a Method?

# Calling methods on objects executes functions that operate on attributes of a specific instance of the class. This means that calling a method on a list, for example,
# only modifies that instance of a list, and not all lists globally. We can define methods within a class by creating functions inside the class definition. These
# instance methods can take a parameter called self which represents the instance the method is being executed on. This will allow you to access attributes of the instance
# using dot notation, like self.name, which will access the name attribute of that specific instance of the class object. When you have variables that contain different
# values for different instances, these are called instance variables.


# In this code, there's a Person class that has an attribute name, which gets set when constructing the object. Fill in the blanks so that 1) when an instance of
# the class is created, the attribute gets set correctly, and 2) when the greeting() method is called, the greeting states the assigned name.
# %%
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is " + self.name


# Create a new instance with a name of your choice
some_person = Person("Osborne")

# Call the greeting method
print(some_person.greeting())


# A docstring is a brief text that explains what something does.
# %%
class Piglet:
    """Represents a piglet that can say their name."""
    years = 0
    name = ""

    def speak(self):
        """Outputs a message including the name of the piglet."""
        print("Oink! I'm {}! Oink!".format(self.name))

    def pig_years(self):
        """Converts the current age to  equivalent pig years."""  # A docstring is a brief text that explains what something does.
        return self.years * 18
    help(pig_years)  # Call docstring


# The code below defines an Elevator class. The elevator has a current floor, it also has a top and a bottom floor that are the minimum and maximum floors
# it can go to. Fill in the blanks to make the elevator go through the floors requested.
# %%
class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current

    def __str__(self):
        """Information about Current floor"""
        return "Current floor: {}".format(self.current)

    def up(self):
        """Makes the elevator go up one floor."""
        if self.current < 10:
            self.current += 1

    def down(self):
        """Makes the elevator go down one floor."""
        if self.current > 0:
            self.current -= 1

    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        if floor >= self.bottom and floor <= self.top:
            self.current = floor
        elif floor < 0:
            self.current = 0
        else:
            self.current = 10


elevator = Elevator(-1, 10, 0)


elevator.down()
elevator.current  # should output 1

elevator.down()
elevator.current  # should output 0

elevator.go_to(10)
elevator.current  # should output 10


# Let???s create a new class together and inherit from it. Below we have a base class called Clothing. Together, let???s create a second class, called Shirt,
# that inherits methods from the Clothing class. Fill in the blanks to make it work properly.
# %%
class Clothing:
    material = ""

    def __init__(self, name):
        self.name = name

    def checkmaterial(self):
        print("This {} is made of {}".format(self.name, self.material))


class Shirt(Clothing):
    material = "Cotton"


polo = Shirt("Polo")
polo.checkmaterial()


# Your mission: Finish the "Stock_by_Material" method and iterate over the amount of each item of a given material that is in stock. When you???re finished, the script
# should add up to 10 cotton Polo shirts.
# %%
class Clothing:
    stock = {'name': [], 'material': [], 'amount': []}

    def __init__(self, name):
        material = ""
        self.name = name

    def add_item(self, name, material, amount):
        Clothing.stock['name'].append(self.name)
        Clothing.stock['material'].append(self.material)
        Clothing.stock['amount'].append(amount)

    def Stock_by_Material(self, material):
        count = 0
        n = 0
        for item in Clothing.stock['material']:
            if item == material:
                count += Clothing.stock['amount'][n]
                n += 1
        return count


class shirt(Clothing):
    material = "Cotton"


class pants(Clothing):
    material = "Cotton"


polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)


# Let???s expand a bit on our Clothing classes from the previous in-video question. Your mission: Finish the "Stock_by_Material" method and iterate over the amount of
# each item of a given material that is in stock. When you???re finished, the script should add up to 10 cotton Polo shirts.
# %%
class Clothing:
    stock = {'name': [], 'material': [], 'amount': []}

    def __init__(self, name):
        material = ""
        self.name = name

    def add_item(self, name, material, amount):
        Clothing.stock['name'].append(self.name)
        Clothing.stock['material'].append(self.material)
        Clothing.stock['amount'].append(amount)

    def Stock_by_Material(self, material):
        count = 0
        n = 0
        for item in Clothing.stock['___']:
            if item == material:
                count += Clothing.___['amount'][n]
                n += 1
        return count


class shirt(Clothing):
    material = "Cotton"


class pants(Clothing):
    material = "Cotton"


polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)


# Modules

# %%
random.randint(1, 10)
# %%
now = datetime.datetime.now()
print(now)


# We have two pieces of furniture: a brown wood table and a red leather couch. Fill in the blanks following the creation of each Furniture class instance, so that
# the describe_furniture function can format a sentence that describes these pieces as follows: "This piece of furniture is made of {color} {material}"
# %%
class Furniture:
    color = ""
    material = ""


table = Furniture()
table.color = "brown"
table.material = "wood"

couch = Furniture()
couch.color = "red"
couch.material = "leather"


def describe_furniture(piece):
    return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))


print(describe_furniture(table))
# Should be "This piece of furniture is made of brown wood"
print(describe_furniture(couch))
# Should be "This piece of furniture is made of red leather"


# The City class has the following attributes: name, country (where the city is located), elevation (measured in meters), and population (approximate, according to recent statistics).
#  Fill in the blanks of the max_elevation_city function to return the name of the city and its country (separated by a comma), when comparing the 3 defined instances for a
# specified minimal population. For example, calling the function for a minimum population of 1 million: max_elevation_city(1000000) should return "Sofia, Bulgaria".
# %%
class City:  # define a basic city class
    name = ""
    country = ""
    elevation = 0
    population = 0


# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509


def max_elevation_city(min_population):
    # Initialize the variable that will hold
    # the information of the city with
    # the highest elevation
    return_city = City()

    # Evaluate the 1st instance to meet the requirements:
    # does city #1 have at least min_population and
    # is its elevation the highest evaluated so far?
    if city1.population >= min_population and city1.elevation > return_city.elevation:
        return_city = city1
    # Evaluate the 2nd instance to meet the requirements:
    # does city #2 have at least min_population and
    # is its elevation the highest evaluated so far?
    if city2.population >= min_population and city2.elevation > return_city.elevation:
        return_city = city2
    # Evaluate the 3rd instance to meet the requirements:
    # does city #3 have at least min_population and
    # is its elevation the highest evaluated so far?
    if city3.population >= min_population and city3.elevation > return_city.elevation:
        return_city = city3

    # Format the return string
    if return_city.name:
        return "{}, {}".format(return_city.name, return_city.country)
    else:
        return ""


print(max_elevation_city(100000))  # Should print "Cusco, Peru"
print(max_elevation_city(1000000))  # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000))  # Should print ""


# %%
for num in range(1, 101):
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
