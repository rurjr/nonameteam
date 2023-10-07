meal_price = float(input("Enter the price of the meal: грн "))
percent_tip = float(input("Enter the percent tip you want to leave: % "))
tip_sum = (percent_tip/ 100) * meal_price
total_bill = meal_price + tip_sum

print(f"Tip sum:  {tip_sum} грн ")
print(f"Total bill with tip: {total_bill} грн")
