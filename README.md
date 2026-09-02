# Python Age Verification Program

## About the Project

This is a beginner Python project that determines whether a user is old enough to access a website based on their birthdate.

The user enters their birthday in `MM/DD/YYYY` format. The program uses the current date to calculate the user's age and determines whether they meet the minimum age requirement of 18.

## Features

- Accepts a birthday in `MM/DD/YYYY` format
- Separates the month, day, and year from the user's input
- Uses the current date to calculate the user's age
- Accounts for whether the user's birthday has occurred yet this year
- Displays the user's birthdate in a readable format
- Displays the user's calculated age
- Grants access to users who are 18 or older
- Denies access to users who are under 18

## Example

```text
Hello, welcome to the website. You must be 18 or older to access this site.
Enter your birthday (MM/DD/YYYY): 06/27/2006

You were born on June 27, 2006
You are 20 years old.
Access granted, please proceed to the website.
```

## What I Learned

While creating this project, I practiced several Python fundamentals, including:

- Variables
- User input
- Converting strings to integers
- Splitting strings with `.split()`
- `if`, `elif`, and `else` statements
- Comparison operators
- Importing and using Python's `datetime` module
- Calculating a person's age using the current date

I also learned why subtracting the birth year from the current year is not always enough to determine someone's exact age. The program checks whether the user's birthday has occurred yet during the current year and adjusts their age when necessary.

## Future Improvements

Some improvements I plan to make as I learn more Python include:

- Detecting invalid dates
- Preventing future dates from being entered as birthdays
- Allowing the user to try again after entering invalid information
- Improving input validation and error handling

## Requirements

- Python 3

No additional packages are required.

## How to Run

1. Download or clone this repository.
2. Open the project in a Python-supported editor or terminal.
3. Run `Age_Verification.py`.
4. Enter your birthday when prompted.
