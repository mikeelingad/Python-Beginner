# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_input = int(age)
years_remaining = 90 - age_input 
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining  * 12 

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and  {months_remaining} left"

print(message)

#### how many days left exercise