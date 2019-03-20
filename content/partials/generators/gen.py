def gen():
  for x in range(10**10000):
    yield x**2

g = gen()
print(g)
print(next(g))
print(next(g))
print(next(g))