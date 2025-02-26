# Set Comprehension - Unique Characters in a String

text = 'Hello World!'

print(set(x.lower() for x in text if x.isalpha()))