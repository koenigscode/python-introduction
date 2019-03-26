# "r" opens the file in read-only mode
f = open("file.txt", "r")
content = f.read()
print(content)
f.close()