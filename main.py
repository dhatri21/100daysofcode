print("Welcome to the Tip Calculator!")
bill_amt = input("What was the total bill?\n")
tip_perc = input("What percentage tip would you like to give? 10, 12 or 15\n")
people = input("How many people to split the bill\n")

tip_total = (float(bill_amt) * int(tip_perc)) / 100

tip = round((tip_total / int(people)),2)

print(f"Each person should pay {tip}$")