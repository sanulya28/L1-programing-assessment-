import random

def yes_no(question):

    """Checks user response to a question is yes / no (y/n), returns 'yes' or 'no'"""

    while True:

        response = input(question).lower()

        # check the user says yes / no/ y / n
        if response == "yes" or response == "y":
           return "yes"
        elif response == "no" or response == "n":
           return "no"
        else:
            print("please enter yes / no")

def instructions():


        print('''
    *** Instructions ***

    You will be asked a series of addition and subtraction questions.

    - Enter the number of questions you want to answer.
    - Type your answer as a whole number.
    - You will be told if your answer is correct or incorrect.

    At the end:
    - You will see your final score as a percentage.
    - You can choose to view your quiz history.

    Good luck!
    ''')


# Main routine
print()
print("\n➕➕➕ Welcome to the Addition and Subtraction Quiz ➖➖➖\n")

# Ask if user wants instruction

want_instructions = yes_no("Do you want to see the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
     instructions()

print("program continues...")

MAX_NUMBER = 20

def get_integer(question):
    """Gets a valid integer from the user."""

    while True:
        try:
            return int(input(question))
        except ValueError:
           print("please enter a valid number.")


def generate_question():
        """Generate a random addition and subtraction question."""

        num1 = random.randint(1, MAX_NUMBER)
        num2 = random.randint(1, MAX_NUMBER)
        operator = random.choice(["+", "-"])

        # prevent negative answers
        if operator == "-" and num2 > num1:
            num1, num2 = num2, num1

        if operator == "+":
            answer = num1 + num2
        else:
            answer = num1 - num2

        question = f"{num1} {operator} {num2}"
        return question, answer

num_questions = get_integer("How many questions do you want? ")

while num_questions <= 0 or num_questions > 20:
    print("Please enter a number between 1 and 20.")
    num_questions = get_integer("How many questions do you want? ")

# setup variables

score = 0
history = []


for item in range(num_questions):

    question, correct = generate_question()

    print(f"\nQuestion {item + 1} of {num_questions}")
    print(question)

    user_answer = get_integer("Your answer: ")

    if user_answer == correct:
        print("Correct!")
        score += 1
        result = True
    else:
        print(f"Wrong! Correct answer: {correct}")
        result = False


# quiz history
if yes_no("Do you want to see your history? ") == "yes":
    percentage = (score / num_questions) * 100
    print(f"You got {score} out of {num_questions} correct.")
    print(f"\nFinal Score: {percentage:.1f}%")


print("\n📜 Quiz History 📜")
for i, item in enumerate(history, 1):
         print(f"\nQuestion {item}: {item['question']}")
         print(f"Correct answer: {item['correct']}")

         if item["result"]:
                print("Correct ✅")
                print("Good Job!!🎉")
         else:
                print(f"Your answer: {item['user']} ❌")
                print("Better luck next time😢")
