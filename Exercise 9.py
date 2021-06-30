# https://www.udemy.com/course/solving-exercises-with-python
# Exercise 9: Print the following pattern:
#      *
#     **
#    ***
#   ****
#  *****

for i in range(0,6):
    print((" " * (5-i)) + ("*" * i))
