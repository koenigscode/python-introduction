def primes_generator():
    yield 2  # yield two

    number = 3  # then start with 3
    while True:
        for div in range(2, number):
            if number % div == 0:
                number += 1
            else:
                yield number  # yield the prime number
                number += 1


# get an instance of the generator
primes = primes_generator()
print(f"primes object: {primes}")

# print first 10 primes
for i in range(10):
    print(next(primes))