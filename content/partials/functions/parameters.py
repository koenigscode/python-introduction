# receives two ints, returns a list
def quotient_and_remainder(divisor: int = 1, dividend: int = 1) -> []:
    return [divisor/dividend, divisor % dividend]


print(quotient_and_remainder(5, 3))
print(quotient_and_remainder(7))
print(quotient_and_remainder())
print(quotient_and_remainder(divisor=7))