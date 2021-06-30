# https://www.udemy.com/course/solving-exercises-with-python
# Exercise 10: Print the following pattern:
# 1
# 12
# 123
# 1234
# 12345

for i in range(0,6):
    for n in range(1, i+1):
        print(n, end="")
    print()