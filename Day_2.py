# Bill Calculator

print("Welcome to the Bill Calculator")

total_bill = float(input("What is your total bill? ₹ "))

tip_percent = int(input("What percentage tip would you like to give?  10, 12 or 15? "))

no_of_people = int(input("How many people to split the bill? "))

total_bill_with_tip = (tip_percent/100 + 1) * total_bill

print(f"Each person should pay: ₹{round(total_bill_with_tip)/no_of_people}")