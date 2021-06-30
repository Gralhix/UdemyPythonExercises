# https://www.udemy.com/course/solving-exercises-with-python
# Exercise 5: Reverse the following list using for loop:
# list1 = [10, 20, 30, 40, 50]

list1 = [10, 20, 30, 40, 50]
list2 = []

for i in list1[::-1]:
    list2.append(i)
print(list2)
    