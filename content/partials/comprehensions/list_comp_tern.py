# if the character is not a blank, add it to the list
# if it already is an uppercase character, leave it that way,
# otherwise make it one
l = [c if c.isupper() else c.upper()
     for c in "This is some Text" if not c == " "]
print(l)
# join the  list and put "" (nothing) between each item
print("".join(l))
