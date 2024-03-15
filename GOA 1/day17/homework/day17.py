
# Write a function that takes a list of numbers as input and returns the sum of all the numbers in the list.

# Write a function that takes a list of strings as input and returns a new list containing only the strings that have a length greater than 5.

# Write a function that takes a list of numbers as input and returns a new list containing only the even numbers from the original list.

# Write a function that takes a list of numbers as input and returns the largest number in the list.

# Write a function that takes a list of strings as input and returns a new list containing only the strings that start with the letter 'a'.

# Write a function that takes a list of numbers as input and returns a new list containing the square of each number.

# Write a function that takes a list of strings as input and returns a new list containing the lengths of each string.

# Write a function that takes a list of numbers as input and returns the sum of all the numbers that are greater than 10. 



def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

number = int(input("Enter a whole number: "))

result = factorial(number)

print("Factorial of", number, "is", result)
