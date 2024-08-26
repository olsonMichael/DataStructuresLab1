#Using anything other than what we learned, please add a comment that explains what you are using and be able to answer it differently.
#Worth 5 points - due friday 8/30 before class. 5 points for a in-person quiz friday about similar tasks.

#1. Write a function reverse_and_uppercase(input_str) that takes a string, reverses it, and converts it to uppercase.
def reverse_and_uppercase(input_str):
    input_str.upper()
    input_str=input_str[::-1]
print(reverse_and_uppercase("hello")
assert reverse_and_uppercase("hello") == "OLLEH"
assert reverse_and_uppercase("DataStructures") == "SERUTCURTSATAD"

#2. Write a function basic_operations(a, b) that returns a tuple containing the sum, difference, product, and quotient of a and b.
def basic_operations(a, b):
    # Your code here

assert basic_operations(10, 2) == (12, 8, 20, 5)

#3. Write a function check_sign(number) that returns "Positive", "Negative", or "Zero" based on the input number.
def check_sign(number):
    # Your code here

assert check_sign(5) == "Positive"
assert check_sign(-3) == "Negative"
assert check_sign(0) == "Zero"

#4. Write a function sum_of_evens(numbers) that returns the sum of all even numbers in a list.
def sum_of_evens(numbers):
    # Your code here

assert sum_of_evens([1, 2, 3, 4, 5, 6]) == 12
assert sum_of_evens([7, 8, 9, 10]) == 18

#5. Write a recursive function fibonacci(n) that returns the nth Fibonacci number. Without recursion. Must use loop.
def fibonacci(n):
    # Your code here

assert fibonacci(5) == 5
assert fibonacci(10) == 55

#6. Write a function parse_and_calculate(expression) that takes a mathematical expression in string format (e.g., "3+5*2-4/2") and returns the result. Handle the operations with the correct order of precedence.
def parse_and_calculate(expression):
    # Your code here

assert parse_and_calculate("3+5*2-4/2") == 10
assert parse_and_calculate("10-3*2+8/4") == 6
