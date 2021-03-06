# ๐จ Don't change the code below ๐
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# ๐จ Don't change the code above ๐

#Write your code below this line ๐
height_float = float(height)
weight_float = float(weight)

bmi = weight_float / (height_float ** 2)

print(int(bmi))

"""
weight_as_int = int(weight)
height_as_float = float(height)

# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2
# or using multiplication and PEMDAS
bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)

print(bmi_as_int)

"""
"""
## BMI Calculator

# UPDATE
We've moved away from repl.it for coding exercises.
Check out the new exercises on Coding Rooms with automated submissions.

Login to your Udemy course and head over to the link below to get the sign up link:

[Click here](https://www.udemy.com/course/100-days-of-code/learn/lecture/17825914#questions)

# Instructions

Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

![](https://cdn.fs.teachablecdn.com/jKHjnLrNQjqzdz3MTMyv)

**Warning** you should convert the result to a whole number. 

# Example Input

```
weight = 80
```

```
height = 1.75
```

# Example Output

80 รท (1.75 x 1.75) =  26.122448979591837

```
26
```

e.g. When you hit **run**, this is what should happen:  

![](https://cdn.fs.teachablecdn.com/wmjVjddeSmGj0QVtOUrE)

# Hint

1. Check the data type of the inputs.
2. Try to use the exponent operator in your code.
3. Remember PEMDAS.
4. Remember to convert your result to a whole number (int). 

# Test Your Code

Before checking the solution, try copy-pasting your code into this repl: 

[https://repl.it/@appbrewery/day-2-2-test-your-code](https://repl.it/@appbrewery/day-2-2-test-your-code)

This repl includes my testing code that will check if your code meets this assignment's objectives. 



# Solution

[https://repl.it/@appbrewery/day-2-2-solution](https://repl.it/@appbrewery/day-2-2-solution)
"""