
def count_divisors(number):

    count =0

    for i in range(1,number+1):
        if number % i == 0:
            count = count + 1
    return count





assert count_divisors(1) == 1
assert count_divisors(6) == 4
assert count_divisors(7) == 2

number = int(input("Enter a number: "))
result = count_divisors(number)
print(f"Number of divisors: {result}")