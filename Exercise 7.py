# https://www.udemy.com/course/solving-exercises-with-python
# Exercise 7: Find the factorial of any number

n = int(input("Please provide a number:\n> "))
fact = 1

for i in range(1,n+1):
    fact = fact * i
    
print(fact)