
def digit_sum(number):
    total = 0

    while number > 0:
        digit = number % 10
        total = total + digit
        number = number // 10

    return total


assert digit_sum(0) == 0
assert digit_sum(507) == 12
assert digit_sum(1111) == 4

number = int(input("Enter a non-negative integer: "))
result = digit_sum(number)

print(f"Digit sum: {result}")
