parcel = int(input("Enter the parcel weight, or 0 to finish: "))
total = 0
count = 0
while parcel > 0:
    total = total + parcel
    parcel =  int(input("Enter the parcel weight, or 0 to finish: "))

    count = count + 1
print (f"Parcels: {count}")
print(f"Total weight: {total} kg")
