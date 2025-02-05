import random

def guess(num):
    number = random.randint(1, 100)
    if num == number:
        return "You have guessed it right!"
    else:
        return f"You have guessed it wrong! The number was {number}"
    