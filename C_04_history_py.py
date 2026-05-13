history=[]

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

# Show history
if yes_no("Do you want to see your history? ") == "yes":
    for i, item in enumerate(history, 1):
            print(f"\nQuestion {i}: {item['question']}")
            print(f"Correct answer: {item['correct']}")

            if item["result"]:
                print("Correct ✅")
            else:
                print(f"Your answer: {item['user']} ❌")

