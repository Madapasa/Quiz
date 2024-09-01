import time
questions = ("What is the capital of France?:", "Which planet is known as the Red Planet?:",
              "Who wrote the play Romeo and Juliet?:", "What is the chemical symbol for water?:")

options = (("a. berlin", "b. madrid", "c. malmö", "d. paris"),
             ("a. Earth", "b. mars", "c. venus", "d. jupiter"), 
             ("a. William Shakespeare", "b. Oscar Wilde", "c. William Words", "d. John Steinbeck"), 
             ("a. H2O", "b. O2", "c. N2", "d. CO2"))

answers = ("d", "b", "a", "a")
guesses = []
score = 0
question_number = 0

for question in questions:
    print("-------------------------------")
    print(question)
    for option in options [question_number]:
        print(option)
    
    guess = input("Enter (a, b, c, d):").lower()
    guesses.append(guess)
    if guess == answers[question_number]:
        score += 1
        print("CORRECT ANSWER")
    else:
        print("WRONG ANSWER")
        print(f"THE CORRECT ANSWER WAS {answers[question_number]}!")
    question_number += 1


print(f"YOUR FINAL SCORE WAS {score}")
time.sleep(3)
print("Goodbye!")
quit()


    