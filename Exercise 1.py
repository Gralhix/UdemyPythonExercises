# https://www.udemy.com/course/solving-exercises-with-python
# Exercise 1: Given two integer numbers return their product. If the product is greater than 1000, then return their sum.


a = int(input("Please enter the first number:\n > "))
b = int(input("Please enter the second number:\n > "))

if int(a * b) > 1000:
    print("The sum between the first and the second number is:", (a + b))
else:
    print("The product between the first and the second number is:", (a * b))
