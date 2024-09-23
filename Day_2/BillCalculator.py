print("Welcome to the tip calculator")

total_bill = float(input("What was the total bill? $"))
tipPercentage = int(input("How much tip would you like to give? 10,12, or 15?"))
number_of_people= int(input("How many people to split the bill?"))
finalTip = total_bill * (tipPercentage/100)
total_bill_with_tip = finalTip + total_bill
total_bill_per_person = round((total_bill_with_tip / number_of_people),2)

print(f"Each person should pay : $ {total_bill_per_person}")