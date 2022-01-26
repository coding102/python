# %%
# Print String 5 times
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