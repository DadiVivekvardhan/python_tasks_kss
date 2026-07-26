#Q. Write a recursive function to reverse a string.

def reverse_string(s):
    if s == "":
        return ""
    else:
        return reverse_string(s[1:]) + s[0]

text = input("Enter a string: ")
print("Reversed string:", reverse_string(text))
