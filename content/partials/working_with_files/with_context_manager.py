with open("file.txt", "r") as f:
    content = f.read()
    print(content)
    print(f"The file is {'closed' if f.closed else 'open'}")

# outside the context manager
print(f"The file is {'closed' if f.closed else 'open'}")