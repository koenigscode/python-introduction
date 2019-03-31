try:
    print("text " + 3)
except TypeError as e:
    print(e)
finally:
    print("This will always be printed out")