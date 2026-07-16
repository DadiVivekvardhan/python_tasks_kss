#Q. Write a program to convert a tuple to a list and modify the element.

t = (10, 20, 30, 40)

l = list(t)
l[1] = 25

print("Modified list:", l)
