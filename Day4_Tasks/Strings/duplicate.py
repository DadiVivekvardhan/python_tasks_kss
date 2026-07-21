#Q. Write a program to remove duplicate characters from a string.

text = "lets go"

result =""

for ch in text:
    if ch not in result:
        result += ch

print("String after removing duplicates:", result)
