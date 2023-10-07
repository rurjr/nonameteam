length_cm = float(input("Enter a length in centimeters: "))
if length_cm < 0:
    print("Invalid entry, length cannot be negative.")
else:
    length_inches = round(length_cm / 2.54, 2)
    print(f"{length_cm} centimeters is equal to {length_inches} inches")
