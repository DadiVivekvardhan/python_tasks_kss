#Q. Write a program to remove duplicate elements from a list.

numbers = [10, 20, 30, 20, 40, 30, 50]

new_list = []

for i in numbers:
    if i not in new_list:
        new_list.append(i)

print(new_list)
