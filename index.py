# 1. If else and if else ladder
# a. Easy Questions:
# i. Write a program to check if a given number is positive,
# negative, or zero.
def check_num(num):
    if num == 0:
        return "zero"
    elif num > 0:
        return "positive"
    elif num < 0:
        return "negative"
        
num = int(input("enter a number:"))
res = check_num(num)
print(res)

# Determine if a number is odd or even
def check_num(num1):
    if (num1 < 0) or (num1 == 0):
        return "enter a valid num"
    elif num1 % 2 == 0:
        return "even"
    else:
        return "odd"
   
        
num1 = int(input("enter a number:"))
res = check_num(num1)
print(res)

# Check if a person is eligible to vote (age >= 18).
def check_age(age):
    if age < 18:
        return "you are not eligible,minor"
    else:
        return "you are eligible for vote"
    
        
age = int(input("enter your age:"))
res = check_age(age)
print(res)

# Write a program to find the greatest of two numbers
def greatest_num(num1,num2):
    if num1 > num2:
        return num1,"is greatest"
    else:
        return num2,"is greatest"
    
num1 = int(input("enter num1:"))
num2 = int(input("enter num2:"))
res = greatest_num(num1,num2)
print(res)

# Write a program to display the day of the week based on a
# number input (1 for Monday, 2 for Tuesday, etc.).
def week_days(day_num):
    if (day_num > 7) or (day_num <= 0):
        return "enter valid number"
    elif day_num == 1:
        return "MONDAY"
    elif day_num == 2:
        return "TUESDAY"
    elif day_num == 3:
        return "WEDNESDAY"
    elif day_num == 4:
        return "THURSDAY"
    elif day_num == 5:
        return "FRIDAY"
    elif day_num == 6:
        return "SATURDAY"
    elif day_num == 7:
        return "SUNDAY"

day_num = int(input("enter a number to know the day:"))
print(week_days(day_num))

# Implement a simple calculator to perform addition,
# subtraction, multiplication, and division.
def cal(user_in):
    if user_in in ["+","add","addition"]:
        return a+b
    elif user_in in ["-",'sub','substraction']:
        return a-b
    elif user_in in ["*","mul","multiplication"]:
        return a*b
    elif user_in in ["/","div","division"]:
        return a/b
    
        
user_in = input("enter the operation:").lower()
a = int(input("enter a num1:"))
b = int(input('enter a num2:'))
print(cal(user_in))
    
# b. Medium Q uestions:
# i. Write a program to find the greatest of three numbers.
def greatest_num(a,b,c):
    if a > b:
        return a,"is greatest num"
    elif b > c:
        return b,"is greatest num"
    elif c > a:
        return c,"is greatest num"
a = int(input('enter a number1 to find greatest one:'))
b = int(input('enter a number2 to find greatest one:'))
c = int(input('enter a number3 to find greatest one:'))
print(greatest_num(a,b,c))   

# ii. Check if a year is a leap year.
def leap_year(year):
    if ((year % 4 == 0) and (year % 100 != 0)) or year % 400 == 0:
        return "leap year"
    else:
        return "not leap"
year = int(input('enter a year: '))
print(leap_year(year))

# iii. Write a program to classify a character entered by the user
# as a vowel, consonant, or neither.
def ver_char(char):
    if len(char) != 1:
        return "enter a single character"
    elif char in ["a","e","i","o","u"]:
        return "vowel"
    elif char.isalpha():
        return "consonant"
    else:
        return "either number or special charectar"

char = input("enter a char:")
print(ver_char(char))


# iv. Calculate the grade of a student based on the marks they
# score:
# 1. 90-100: Grade A
# 2. 80-89: Grade B
# 3. 70-79: Grade C
# 4. <70: Fail.
def result(marks):
    if 90 <= marks <= 100:
        return "Grade A"
    elif 80 <= marks <= 89:
        return "Grade B"
    elif 70 <= marks <= 79:
        return "Grade C"
    elif marks < 70:
        return "Fail"
marks = int(input("enter your marks:"))
print(result(marks))


# v. Write a program to check if three sides length form a valid
# triangle.
def triangle(a,b,c):
    if (a+b > c) and (b+c > a) and (a+c > b):
        return "it forms a triangle"
    else:
        return "it does not forms a triangle"
a = int(input('enter one side of triangle:'))
b = int(input('enter second side of triangle:'))
c = int(input('enter third side of triangle:'))
print(triangle(a,b,c))

# 2. Loops:
# a. Easy Questions:

# i. Print all numbers from 1 to 100 using a for loop
def allnum(nums):
    for i in range(nums+1):
        print(i)
nums = int(input("enter number:"))
print(allnum(nums))

# Write a program to print the sum of the first n natural
# numbers. (n*n+1/ 2)
def natural_num(num):
    sum = 0
    for i in range(num+1):
        sum += i
    return sum

num = int(input("enter a num:"))
print(natural_num(num)) 
# 2nd method
def natural_num(n):
    if n < 0:
        return "enter a +ve num"
    return (n*(n+1))//2

n = int(input("enter a num:"))
print(natural_num(n))

# iii. Print all even numbers between 1 and 50 using a while
# loop
def even_nums(n):
    for i in range(1,n+1):
        if i % 2 == 0:
            print(i)
n = int(input("enter a num:"))
print(even_nums(n))
# using while loop 
def even_nums(n):
     num = 1
     while num <= n:
         if num % 2 == 0:
             print(num)
         num += 1     
         
n = int(input("enter a num:"))
print(even_nums(n))


# Write a program to display the multiplication table of a given
# number. First 20
def multiplication(num):
    mul = 1
    for i in range(1,21):
        mul = num * i
        print(num,"*",i,"=",mul)
num = int(input("enter a number:"))
multiplication(num)

# multiplication tables upto 20
def multiplication():
    for j in range(1,21):
        for i in range(1,11):
            mul = j * i
            print(j,"*",i,"=",mul)
multiplication()




# v. Reverse a number using a while loop.
# 1. Also can we get the sum of all the digits
def reverse_num(num):
    rev_num = 0
    sum = 0
    while num > 0:
        rem = num % 10
        num = num // 10
        sum += rem
        rev_num = rev_num * 10 + rem
    print(rev_num)
    print(sum)
    
num = int(input('enter a num:'))
reverse_num(num)
        

# vi. Write a program to count the number of digits in a given
# number using a while loop    
def digits_in_num(num):
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    print(count)
    
num = int(input('enter a num:'))
digits_in_num(num)

# vii. Write a program that keeps asking the user to enter numbers
# until they enter a negative number. Use a while loop.
def numbers():
    num = 0
    while num >= 0:
        num = int(input('enter a number (if you enter negative number loop will break):'))
    
numbers()

# Print the first 10 terms of the Fibonacci series using a for
# loop.
def fabonacci(num):
    a = 0
    b = 1
    for _ in range(num):
        print(a,end=" ")
        a,b = b, a+b
num = int(input('enter a num:'))
fabonacci(num)        
   
# ii. Check if a given number is a prime number using a for loop.            
def prime(num):
    if num < 2:
        print("not prime")
        return
    count = 0
    for i in range(1,num+1):
         if num % i == 0:
             count += 1
    if count == 2:
        print('prime')
    else:
        print('not a prime')

num = int(input('enter a num:'))
prime(num)

# 2nd method for prime
def prime(num):
    if num < 2:
        print("not prime")
        return
    flag = True
    for i in range(2,num):
        if num % i == 0:
            flag = False
            break
    if(flag):
        print("prime")
    else:
        print('not a prime')
num = int(input('enter a num:'))
prime(num)
    
# iii. Write a program to calculate the factorial of a number using
# a while loop.   
def facto(num):
    fact = 1
    while num > 1:
        fact *= num
        num -= 1
    print(fact)  
num = int(input('enter a num:'))
facto(num)

# iv. Print all numbers from 1 to 100 that are divisible by 3 and 5
# using a for loop
def divisible():
    for i in range(1,101):
        if i % 5 == 0:
            print(i,'is divisible by 5')
        elif i % 3 == 0:
            print(i,'is divisible by 3')
divisible()            

# v. Implement a menu-driven program where the user can
# choose to:
# 1. Find the square of a number.
# 2. Find the cube of a number.
# 3. Exit.
def user_ip():
    while True:
        user = input('enter the operation square,cube,exit: ').lower()
        if user == 'exit':
            break
        elif user == 'square':
            n = int(input('enter a num:'))
            n = n*n
            print(n)
        elif user == 'cube':
             n = int(input('enter a num:'))
             n = n*n*n
             print(n)
            
            
user_ip()  

# vi. Implement a basic login system where the user has three
# attempts to enter the correct password using a loop.
def user_attempts():
    attempts = 3
    user_password = 'sandhya'
    while attempts > 0:
        user_trial = input('enter your password:')
        if user_trial == user_password:
            print('login success')
            break
        else:
            print('invalid')
            attempts -= 1
user_attempts()            
    
    
   
      
    
   
               
        
    