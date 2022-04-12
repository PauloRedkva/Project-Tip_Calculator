# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_int = int(age)
age_final = int(90)
rest_life = age_final - age_int
days = int(rest_life * 365)
weeks = int(rest_life * 52)
months = int(rest_life * 12)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")

"""

years = 90 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")

"""



"""## 
Your Life in Weeks

# UPDATE
We've moved away from repl.it for coding exercises.
Check out the new exercises on Coding Rooms with automated submissions.

Login to your Udemy course and head over to the link below to get the sign up link:

[Click here](https://www.udemy.com/course/100-days-of-code/learn/lecture/17825914#questions)

# Instructions

I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

[https://waitbutwhy.com/2014/05/life-weeks.html](https://waitbutwhy.com/2014/05/life-weeks.html)

Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old. 

It will take your current age as the input and output a message with our time left in this format:

> You have x days, y weeks, and z months left. 

Where x, y and z are replaced with the actual calculated numbers. 

 

**Warning** your output should match the Example Output format exactly, even the positions of the commas and full stops. 

# Example Input

```
56
```

# Example Output

```
You have 12410 days, 1768 weeks, and 408 months left.
```

e.g. When you hit **run**, this is what should happen:  

 
![](https://cdn.fs.teachablecdn.com/RjqBViZQpyVTv7XY6cfA)
 

# Hint

1. There are 365 days in a year, 52 weeks in a year and 12 months in a year.
2. Try copying the example output into your code and replace the relevant parts so that the sentence is formated the same way.

# Test Your Code

Before checking the solution, try copy-pasting your code into this repl: 

[https://repl.it/@appbrewery/day-2-3-test-your-code](https://repl.it/@appbrewery/day-2-3-test-your-code)

This repl includes my testing code that will check if your code meets this assignment's objectives. 


# Solution

[https://repl.it/@appbrewery/day-2-3-solution](https://repl.it/@appbrewery/day-2-3-solution)
"""