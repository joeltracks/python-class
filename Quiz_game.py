# List containing all the questions, choices and correct answers
import random

Questions = [
    {"text": "How many planets are in the solar system? ",
     "choices": ("A. 8", "B. 9", "C. 4", "D. 2"),
     "answer": "A"},
    {"text": "Which planet is the hottest? ",
     "choices": ("A. Mercury", "B. Venus", "C. Mars", "D. Earth"),
     "answer": "B"},
    {"text": "How long does it take sunlight to reach earth? ",
     "choices": ("A. 2 hrs", "B. 30 min", "C. 8 min", "D. 24 hrs"),
     "answer": "C"},
    {"text": "Which planet is referred to as the red planet? ",
     "choices": ("A. Jupiter", "B. Neptune", "C. Mars", "D. Saturn"),
     "answer": "C"},
    {"text": "What is the furthest planet from the sun? ",
     "choices": ("A. Pluto", "B. Venus", "C. Mercury", "D. Neptune"),
     "answer": "D"}
]

# creating a score variable
score = 0
# Using the random module to shuffle through questions order

random.shuffle(Questions)
# Using for loop to go through questions

for question in Questions:
    print(question["text"])
    print()
    for choice in question["choices"]:
        print(choice)

# requesting and checking user input
    your_answer = input("Enter (A, B, C, D): ").upper()
    valid_answer = ["A", "B", "C", "D"]
# 
    while your_answer not in valid_answer:
        your_answer = input("Enter (A, B, C, D): ").upper()


    if your_answer == question["answer"]:
         score += 1 
         print("CORRECT!") 
    else:
         print("INCORRECT!") 



# Showing final score
print("Quiz complete!!!")


print(f"You got {score} out of 5")  

# Providing feedback based on final score

if score == 5:
     print("Excellent!")

elif score < 5 and score > 2:
     print("Good")
     
else:
     print("Try Again")
