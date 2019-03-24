r = range(1, 10)  # creates a new range object
print(f"range: {r}")  # r is a range object, not a list

try:
  r.add(11)
except AttributeError as e:
  # as r is a range object rather than a list,
  # you can't add an item to it
  print(f"error: {e}")

# as range instances are iterable,
# you can create a normal list from them:
l = list(r)
print(f"list: {l}")