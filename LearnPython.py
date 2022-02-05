# %%
# Print String 5 times
from audioop import mul
from itertools import count


for i in range(5) :
     print("This is fun")





# %%
# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)






# %%
#Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
     print(x)     





# %%
#Print all items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
     print(thislist[i])




# %%
#Print all items, using a while loop to go through all the index numbers
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
     print(thislist[i])
     i = i + 1




# %%
def area_triangle(base, height):
     return base*height/2

area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a + area_b
print("The sum of both areas is: " + str(sum))






# %%
def get_seconds(hours, minutes, seconds):
  return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2,30,0)
amount_b = get_seconds(0,45,15)
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
#branching

if condition1:
	if-block
elif condition2:
	elif-block
else:
	else-block


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

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative





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
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192




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
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
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
		if result > 25 :
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

print(sum_squares(10)) # Should be 285




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
    for i in range(1,n+1):
        result = result * i
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120




# The function sum_positive_numbers should return the sum of all positive numbers between the number n received
# and 1. For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15. Fill 
# in the gaps to make this work:
# %%
#using recursion
def sum_positive_numbers(n):
  if n <= 1:
      return n
  return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15


#using normal functions
def sum_positive_numbers(n):
  sums = 0
  for v in range(1,n+1):
    sums += v
  return sums

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15





# Modify the double_word function so that it returns the same word repeated twice, followed by the length of 
# the new doubled word. For example, double_word("hello") should return hellohello10.
# %%
def double_word(word):
    return word * 2 + str(len(word * 2))

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0



# Want to give it a go yourself? Be my guest! Modify the first_and_last function so that it returns True 
# if the first letter of the string is the same as the last letter of the string, False if they’re different. 
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
def replace_domain(email, old_domain, new_domain): #3 parameters: email address to be checked, old domain, and new domain
     if "@" + old_domain in email: # check if the concat of the @ and old domain are in the email address using "in"
          index = email.index("@" + old_domain) # find index where old domain (including @ sign) starts
          new_email = email[:index] + "@" + new_domain # use the index to create the new email
          return new_email # return new email
     return email # if the email didn't contain new domain just return it




# Fill in the gaps in the initials function so that it returns the initials of the words contained 
# in the phrase received, in upper case. For example: "Universal Serial Bus" should return "USB"; "local area network" 
# should return "LAN”.     
# %%
def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS






# %%
name = "Mark"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))
print("Your lucky number is {number}, {name}.".format(name=name, number=len(name)*3))





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
print (price, with_tax)

print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))




# %%
def to_celsius(x):
     return (x-32)*5/9
for x in range(0,101,10):
     print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x))) #align to right 3 spaces, 2 decimal places and align to the right 6 spaces






#The is_palindrome function checks if a string is a palindrome. A palindrome is a string that can be equally read from left to right or 
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

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True




# Using the format method, fill in the gaps in the convert_distance function so that it returns the phrase "X miles equals Y km", with Y having 
# only 1 decimal place. For example, convert_distance(12) should return "12 miles equals 19.2 km".
# %%
def convert_distance(miles):
	km = miles * 1.6 
	result = "{} miles equals {:.1f} km".format(miles, km)
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km






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

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing




# The skip_elements function returns a list containing every other element from an input list, starting with the first element. Complete this function to do that, 
# using the for loop to iterate through the input list.
#%%
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
		i+= 1

	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []






# Let's use tuples to store information about a file: its name, its type and its size in bytes. Fill in the gaps in this code to return the size in kilobytes
# (a kilobyte is 1024 bytes) up to 2 decimal places. 
# %%
def file_size(file_info):
	name, tpe, size = file_info
	return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21






# %%
animals = ["Lion", "Zebra", "Dolphin", "Monkey"] # iterate over list of strings
characters = 0
for animal in animals: # for each string
     characters += len(animal) # get length and add it to the total amount of characters

print("Total characters: {}, Average length: {}".format(characters, characters/len(animals))) # print total and average by dividing total by the length of the list






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

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']







# write a function that creates a new list containing one string per person including name and email address example: Mark Smith <mark@example.com> 
# %%
def full_emails(people):
     result = []
     for email, name in people:
          result.append("{} <{}>".format(name, email))
     return result

print (full_emails([("alex@example.com", "Alex Smith")]))







# %%

multiples = []
for x in range(1,11):
     multiples.append(x*7)
print (multiples)

# use list comprehension to accomplish the same task as above
# %%
multiples = [ x*7 for x in range(1,11)]
print(multiples)





# list of strings - generate list of lengths of strings
# %%
languages = ["Python", "Ruby", "Java", "Go"]
lengths = [len(language) for language in languages]

print(lengths)





# print all numbers divisible by 3 between 0 and 100
# %%
z = [x for x in range(0,101) if x % 3 == 0]
print (z)





# The odd_numbers function returns a list of odd numbers between 1 and n, inclusively. Fill in the blanks in the function, using 
# list comprehension. Hint: remember that list and range counters start at 0 and end at the limit minus 1.
# %%
def odd_numbers(n):
	return [x for x in range(0,n+1) if x % 2 != 0]
print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []






# Given a list of filenames, we want to rename all the files with extension hpp to the extension h. To do this, we would like to generate 
# a new list called newfilenames, consisting of the new filenames. Fill in the blanks in the code using any of the methods you’ve learned
# thus far, like a for loop or a list comprehension.
# %%
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = [filename.replace(".hpp",".h") for filename in filenames]

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]





# Let's create a function that turns text into pig latin: a simple text transformation that modifies each word moving the first character to 
# the end and appending "ay" to the end. For example, python ends up as ythonpay.
#%%
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
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"








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
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
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
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------






# The group_list function accepts a group name and a list of members, and returns a string with the format: group_name: member1, member2, … For example, 
# group_list("g", ["a","b","c"]) returns "g: a, b, c". Fill in the gaps in this function to do that.
#%%
def group_list(group, users):
  members = ', '.join(users)
  return '{}: {}'.format(group,members)

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"







# The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, and prints the sentence 
# "Guest is X years old and works as __." for each one. For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) 
# should print out: Ken is 30 years old and works as Chef. Pat is 35 years old and works as Lawyer. Amanda is 25 years old and works as Engineer. 
# Fill in the gaps in this function to do that. 
# %%
def guest_list(guests):
	for guest in guests:
		name, age, job = guest
		print("{} is {} years old and works as {}".format(name, age, job))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
# Output should match:
# Ken is 30 years old and works as Chef
# Pat is 35 years old and works as Lawyer
# Amanda is 25 years old and works as Engineer





# Dictionary
# %%
file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
print(file_counts)

file_counts["txt"] # count how many txt files
"jpeg" in file_counts # does the file jpg exist?
file_counts["pdf"] = 10 # add file type and count, if file type already exist count is replaced
print(file_counts)
del file_counts["pdf"] # delete file type
print(file_counts)





# The "toc" dictionary represents the table of contents for a book. Fill in the blanks to do the following: 	1) Add an entry for Epilogue on page 39. 	
# 2) Change the page number for Chapter 3 to 24. 	
# 3) Display the new dictionary contents. 	
# 4) Display True if there is Chapter 5, False if there isn't.
# %%
toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Epilogue"] = 39 # Epilogue starts on page 39
toc["Chapter 3"] = 24 # Chapter 3 now starts on page 24
print(toc) # What are the current contents of the dictionary?
print("Chapter 5" in toc) # Is there a Chapter 5?







#ITERATING over dictionary content
#%%
file_counts = {"jpeg":10, "txt":20, "csv":30, "py":15}
for extension in file_counts:
     print(extension) # will only print key


for ext, amount in file_counts.items(): #print key and value pair using the items() method, it will return a tuple for each element in the dictionary
     print("There are {} files with the .{} extension".format(amount, ext))


file_counts.keys() # return keys
file_counts.values() # return values

# Use items() to get both key and value
# Use keys() to get keys
# Use values() to get values

for value in file_counts.values():
     print(value)



# Complete the code to iterate through the keys and values of the cool_beasts dictionary. Remember that the items method returns a tuple of key, value for each 
# element in the dictionary.
# %%
cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for animals, features in cool_beasts.items():
    print("{} have {}".format(animals, features))







# How times do letters appear in a piece of text?
#%%
def count_letters(text):
     result = {} # initialize an empty dictionary
     for letter in text: # go through each letter in the given string
          if letter not in result: # for each letter check if it's already in the given string
               result[letter] = 0 # if not in dictionary add it 
          result[letter] += 1 # increment the count for that letter in the dictionary
     return result
count_letters("MarkM")







# %%
