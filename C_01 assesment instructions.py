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
print("\n➕➕➕Welcome to the addition and subtraction Quiz➖➖➖/n")
print()

# Ask if user wants instruction

want_instructions = yes_no("Do you want to see the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
     instructions()

print("program continues...")