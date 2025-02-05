import random

def generate_number():
    return random.randint(1, 100)

def guess(num, number):
    if num == number:
        return "You have guessed it right!"
    else:
        return f"You have guessed it wrong! The number was {number}"

# Generate the number once
number = generate_number()

# Get user input
num = int(input("Enter a number between 1 to 100: "))

# Call the function with both arguments
print(guess(num, number))
