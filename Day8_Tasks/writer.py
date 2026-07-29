#5. Word Counter Program
#A writer saves an article in a file called article.txt. Write a Python program that:
#● Opens and reads the file
#● Counts the number of words, lines, and characters in the file
#● Displays the results.

file = open("article.txt", "r")

text = file.read()

file.close()

characters = len(text)

words = len(text.split())

lines = len(text.split("\n"))

print("Number of Characters:", characters)
print("Number of Words:", words)
print("Number of Lines:", lines)
