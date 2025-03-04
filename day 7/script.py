# create a file with some text and then open it and print the content

# file creation
file = open('./randomTextFile.txt', 'w')
file.write('some random text in this new file')
file.close()
print('file is created')

# open file and print content
file = open('./randomTextFile.txt')
print(file.read())