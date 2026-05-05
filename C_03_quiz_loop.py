def get_integer( question):
    """Gets a valid integer from the user."""

    while True:
        try:
            return int(input(question))
        except:
           print("please enter a valid number.")



 num_questions = get_integer("How many questions do you want? ")

while num_questions <= 0:
    print("Please enter a number greater than 0.")
    num_questions = get_integer("How many questions do you want? ")

    for i in range(num_questions):

        question, correct = generate_question()
        print(f"\nQuestion {i + 1}: {question}")

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