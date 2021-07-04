# https://www.udemy.com/course/solving-exercises-with-python
# Exercise 11: Display all prive numbers within a range
# Will use range 1 to 500


for n in range(1, 500):
    for i in range(2, n):
        if (n % i) == 0:
            break
    else:
        print(n)
        
        