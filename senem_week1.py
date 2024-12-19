# Question 1: Write a Python code that prints numbers from 1 to 10 on the screen.
# 
'''
nummer = 0
for nummer in range(0,10):
    nummer += 1
    print(nummer)
    
'''

# Question 2: Take a number input from the user and write a Python program that prints even numbers up to this number on the screen. Do this first with 'for' and then with 'while' loops.

# What if the user enters an odd number?

# version 1
'''
entered_number = int(input('Please enter a number: '))

for number in range(0, entered_number):
    if number % 2 == 0:
        print(number)
        number += 1
'''
#version 2
'''
number = int(input('Please enter a number: '))
displayed_numbers = 0

while displayed_numbers <= number:

    if displayed_numbers % 2 == 0:
        print(displayed_numbers)
    displayed_numbers += 1

'''
# Question 3: Write a Python code that receives a start and end value from the user and prints all the numbers between these values ​​(including the end value) on the screen.

'''
start = int(input('Please enter the start value: '))
end = int(input('Please enter the end value: '))
number = 0

for number in range(start, end):
    number += 1
    print(number)
'''

# Question 4: Get a number from the user and write a Python code that prints whether this number is odd or even.

'''
number = int(input('Please enter a number: '))

if number % 2 == 0:
    print('This is an even number.')
else:
    print('This is an odd number.')
'''

# Question 5: Write a Python program that takes a positive integer input from the user and calculates its factorial. Factorial is the product of all positive integers between a number itself and 1.

'''
number = int(input('Please enter a number: '))
factorial = 1

for i in range(1, number + 1):
    factorial *= i
    i += 1

print('Factorial', factorial)
'''

# Question 6: Write a Python code that receives a number from the user and checks whether this number is prime.

'''
number = int(input("Enter a number: "))

if number < 2:
    print("Not Prime")
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
'''

# Question 7: How to create a loop that calculates the Fibonacci sequence and returns the result as a list containing numbers up to a certain limit?
'''
limit = int(input("Enter a limit: "))
fibonacci_list = [0, 1]

while True:
    next_number = fibonacci_list[-1] + fibonacci_list[-2]
    if next_number > limit:
        break
    fibonacci_list.append(next_number)

print(fibonacci_list)
'''


# Question 8: Write a Python code that takes a word from the user and prints the reverse of this word on the screen.

'''
text = input('Please enter a word: ')

reverse = text[::-1]
print(reverse)

'''

# Question 9: How to create a combination of loop and conditional statement that takes a word input from the user and checks whether that word is a palindrome (the same when read backwards)?

'''
text = input('Please enter a word: ')

reverse = text[::-1]

if text == reverse:
    print('This is a palindrome.')
else:
    print('This is not a palindrome.')

'''

# Question 10: Write the code that calculates the person's weight index and returns the result as underweight, overweight or overweight according to the index value. (You can look on the internet for the weight index calculation)
# To do this, ask the user for their weight and height measurements. weight index
# If it is below 25, it is weak,
# Between 25-30 is normal,
# If you are over 30-40, you are overweight.
# If you are over 40, you are overweight.


'''
weight = float(input('Please enter your weight: '))
height = float(input('Please enter your height: '))

bmi = weight / (height * height)

if bmi < 25:
    print('Underweight')
elif 25 <= bmi < 30:
    print('Normal')
elif 30 <= bmi < 40:
    print('Overweight')
elif bmi >= 40:
    print('Obese')
'''


# Question 11: How to write a Python program that finds the largest of three numbers entered by a user?

'''
number1 = int(input('Please enter the first number: '))
number2 = int(input('Please enter the second number: '))
number3 = int(input('Please enter the third number: '))

if number1 > number2 and number1 > number3:
    print('The largest number:', number1)
elif number2 > number1 and number2 > number3:
    print('The largest number:', number2)
else:
    print('The largest number:', number3)

'''
# Question 12: Get Midterm and Final grades from a student for any course. 
# The sum of 40% of the midterm exam grade and 60% of the final grade will give the year-end average. 
# If the average is below 50, "FAILED" will appear on the screen, and if it is 50 or above, 
# "SUCCESSFUL" will be displayed on the screen. This printing process is 4 lessons. 
# and the lessons will be written one after the other.

'''
for i in range(4):
    lesson = input(f"Enter the lesson {i + 1}: ")
    midterm = int(input(f"Enter the midterm grade for {lesson}: "))
    final = int(input(f"Enter the final grade for {lesson}: "))

    average = midterm * 0.4 + final * 0.6
    if average < 50:
        print(f"{lesson}: FAILED")
    else:
        print(f"{lesson}: SUCCESSFUL")
'''
