with open("multiline_file.txt") as f:
    print(f.read())
    f.seek(0)  # reset stream position
    print("----------")

    print(f.readline(), end="")
    print(f.readline(), end="")
    f.seek(0)  # reset stream position
    print("----------")

    print(f.readlines())
