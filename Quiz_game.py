# Dictionary containing all the questions and correct answers

Questions = {
    "How many planets are in the solar system?: ": "A",
    "Which planet is the hottest?: ": "B",
    "How long does it take sunlight to reach earth?: ": "C",
    "Which planet is referred to as the red planet?: ": "C",
    "What is the furthest planet from the sun?: ": "D"
    }

# tuple with all the available choices

Choices = (("A. 8", "B. 9", "C. 4", "D. 2"),
           ("A. Mercury", "B. Venus", "C Mars", "D. Earth"),
           ("A. 2 hrs", "B. 30 min", "C. 8 min", "D. 24 hrs"),
           ("A. Jupiter", "B. Neptune", "C. Mars", "D. Saturn"),
           ("A. Pluto", "B. Venus", "C. Mercury", "D. Neptune"))

# creating a score and question number variable
Score = 0
Question_num = 0

# Using for loop to go through questions

for Question in Questions:
    print()
    print(Question)
    for choice in Choices[Question_num]:
        print(choice)

# requesting and checking user input
    your_answer = input("Enter (A, B, C, D): ")
    valid_answer = ["A", "B", "C", "D"]

    if your_answer == Questions[Question]:
         Score += 1 
         print("CORRECT!") 
    else:
         print("INCORRECT!") 


    Question_num += 1

# Showing final score
print("Quiz complete!!!")


print(f"You got {Score} out of 5")  

# Providing feedback based on final score

if Score == 5:
     print("Excellent!")

elif Score < 5 and Score > 2:
     print("Good")
     
else:
     print("Try Again")
