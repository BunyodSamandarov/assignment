bin = int(input("Enter bins: "))
total = 0
count = 0
for i in range(1,bin+1):
    bottle = int(input("Enter bottle: "))
    total = total + bottle
    if bottle == 0:
        count = count + 1


print(f"Total bottle: {total}")
print(f"Empty bins: {count}")