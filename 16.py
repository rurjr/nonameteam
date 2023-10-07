def calculate_saving(N):
    saving=300
    monthly_saving=100
    every_six_months_saving=500
    for month in range(1, N + 1):
        saving += monthly_saving
        if month % 6 == 0:
            saving += every_six_months_saving
    return saving
N = int(input("Enter the number of months: "))
total_saving = calculate_saving(N)
print(f"John's savings after {N} months will be {total_saving}")
