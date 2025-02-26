# Set Comprehension - Unique Characters in a String

text = 'Hello World!'

print(dict.fromkeys(x.lower() for x in text if x.isalpha()).keys())