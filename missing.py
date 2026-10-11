a = 8
b = 3

a = a + b
print(f"Stage 1: a = {a}, b = {b}")

b = b * a
print(f"Stage 2: a = {a}, b = {b}")

a = b - a
print(f"Stage 3: a = {a}, b = {b}")
