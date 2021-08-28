print(type(int(str(100))))
a = 100
b= str(a)
c= int(b)
print(type(c))

name = "LaaLa"
age = 45
relationship_status  = "Single"

relationship_status = 'It\'s complicated'
print(relationship_status)

DOB = 1998
# Age ?
user_input = input("Enter your DOB to know your Age : ")
print(type(user_input))
age = 2021 - int(user_input)
print(f"You are {age} years old ")

age = int(input("Enter your Age ?"))

years_remaining = 90- age
days_reaming = years_remaining * 365
weeks_remaining = years_remaining *52
months_remaining = years_remaining * 12
print(f'You have {days_reaming} days, {weeks_remaining} weeks and {months_remaining} months remaining ')