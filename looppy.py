notes_50 = int(input("Enter the number of 50000-so‘m notes: "))
notes_20 = int(input("Enter the number of 20000-so‘m notes: "))
amount = int(input("Enter the withdrawal amount: "))

# Use as many 50,000-so'm notes as possible
use_50 = amount // 50000

# Do not use more notes than the ATM has
if use_50 > notes_50:
    use_50 = notes_50

remaining = amount - use_50 * 50000

if remaining % 20000 == 0 and remaining // 20000 <= notes_20:
    print("Withdrawal possible")

elif use_50 >= 1:
    use_50 = use_50 - 1
    remaining = amount - use_50 * 50000

    if remaining % 20000 == 0 and remaining // 20000 <= notes_20:
        print("Withdrawal possible")
    else:
        print("Withdrawal impossible")

else:
    print("Withdrawal impossible")