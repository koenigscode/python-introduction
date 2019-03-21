def my_sum(*args):
    sum = 0
    for number in args:
        sum += number

    return number


print(my_sum(1, 2, 3))
print(my_sum(1, 2, 3, 4, 5))
