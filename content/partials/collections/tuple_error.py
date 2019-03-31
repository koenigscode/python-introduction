t = 5, 3, -1

try:
    x, y = t
except ValueError as e:
    print(e)

try:
    x, y, z, w = t
except ValueError as e:
    print(e)

x, y, _ = t
print(f"x: {x}, y: {y}")