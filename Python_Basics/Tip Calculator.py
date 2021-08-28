print("Welcome to tip calculator! ")
bill = float(input('What was the total bill ? ₹'))
tip = int(input("How much tip would you like to give ? 10 , 12, 15 : "))
people = int(input('How many people would like to split the bill ? '))
tip_amount = (tip/100)* bill
total_bill = tip_amount + bill
final_amount = total_bill / people
print(f'Each person should pay : ₹{round(final_amount,2)}')
print('Each person should pay :- ₹{:.2f}'.format(final_amount))

















