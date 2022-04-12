#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? $")
tip_to_give = input("How much tip would you like to give? 10, 12, or 15% ? ")
number_people = input("How many people to split the bill? ")

total_bill_float = float(total_bill)
tip_to_give_int = int(tip_to_give)
number_people_int = int(number_people)

tip_calculator = float(total_bill_float / number_people_int) * (tip_to_give_int / 100 + 1)

result = round(tip_calculator, 2)
result = "{:.2f}".format(result)

message = (f"Each person should pay: $ {result}")
print(message)

"""
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)


# FAQ: How to round to 2 decimal places?

# Find the answer in the Q&A here: https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048


print(f"Each person should pay: ${final_amount}")
"""
"""
## Tip Calculator

# Instructions

If the bill was $150.00, split between 5 people, with 12% tip. 

Each person should pay (150.00 / 5) * 1.12 = 33.6

Format the result to 2 decimal places = 33.60

Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.

Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪


# Example Input

```
Welcome to the tip calculator!
What was the total bill? $124.56
How much tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 7
```

# Example Output

```
Each person should pay: $19.93
```


# Hint

1. [How to round a number to 2 decimal places in Python](https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal)
2. [How to limit a float to two decimal places in Python](https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python)



# Solution

[https://replit.com/@appbrewery/tip-calculator-end](https://replit.com/@appbrewery/tip-calculator-end)
"""