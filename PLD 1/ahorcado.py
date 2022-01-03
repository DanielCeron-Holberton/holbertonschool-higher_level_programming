import random

words = ["Holberton", "School", "Hello", "World", "Python"]

word = random.choice(words)
print("Enter a char:")
char = input()
for i in range(len(word)):
    if (char == word[i]):
        print("{:c}".format(i), end="")
    else:
        print("_", end="")
print("")
