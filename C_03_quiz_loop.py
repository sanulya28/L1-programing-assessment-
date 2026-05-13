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

num_questions = get_integer("How many questions do you want? ")

while num_questions <= 0:
    print("Please enter a number greater than 0.")
    num_questions = get_integer("How many questions do you want? ")

# setup variables
score = 0
history = []

# Quiz loop
for i in range(num_questions):

    question, correct = generate_question()
    print(f"\nQuestion {i+1}: {question}")

    user_answer = get_integer("Your answer: ")

    if user_answer == correct:
        print("Correct!")
        score += 1
        result = True
    else:
        print(f"Wrong! Correct answer: {correct}")
        result = False

    # store history
    history.append({
        "question": question,
        "correct": correct,
        "user": user_answer,
        "result": result
    })
