#This program will determine if someone is old enough to access a website based on their birthdate. 
#It will print the persons age as well.
from datetime import date

print("Hello, welcome to the website. You must be 18 or older to access this site.")
birthday = input("Enter your birthday (MM/DD/YYYY): ")

month, day, year = birthday.split("/")

month = int(month)
day = int(day)
year = int(year)

today = date.today()

age = today.year - year

if (today.month, today.day) < (month, day):
       age = age -1

if month == 1:
    print("You were born on January", day, ",", year)
elif month == 2:
    print("You were born on February", day, ",", year)
elif month == 3:    
    print("You were born on March", day, ",", year)
elif month == 4:
    print("You were born on April", day, ",", year)
elif month == 5:
    print("You were born on May", day, ",", year)
elif month == 6:
    print("You were born on June", day,",", year)
elif month == 7:
    print("You were born on July", day, ",", year)
elif month == 8:
    print("You were born on August", day, ",", year)
elif month == 9:
    print("You were born on September", day, ",", year)
elif month == 10:
    print("You were born on October", day, ",", year)
elif month == 11:
    print("You were born on November", day, ",", year)
elif month == 12:
    print("You were born on December", day, ",", year)

if age < 18:
    print("You are" , age , "years old.")
    print("Access denied, you are too young to access this system. Please return to the main menu.")
else:
    print("You are", age, "years old.")
    print("Access granted, please proceed to the website.")

