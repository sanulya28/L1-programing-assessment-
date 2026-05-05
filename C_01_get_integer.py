import random

MAX_NUMBER = 20

def get_integer( question):
    """Gets a valid integer from the user."""

    while True:
        try:
            return int(input(question))
        except:
           print("please enter a valid number.")


def generate_question():
    """Generate a random addition and subtraction question."""

    num1 = random.randint(1, MAX_NUMBER)
    num2 = random.randint(1, MAX_NUMBER)
    operator = random.choice(["+", "-"])

    # prevent negative answers
    if operator == "-" and num2 > num1:
     num1,num2 = num2,num1

    if operator == "+":
     answer = num1 + num2
    else:
     answer = num1 - num2

    question = f"{num1} {operator} {num2}"
    return question, answer
