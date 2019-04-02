f = open("file.txt", "w")

try:
    # use file
except EOFError:
    # handle error appropriately
finally:
    # if the file is not closed yet, do so
    if not f.closed():
        f.close()
