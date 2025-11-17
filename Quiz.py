score = 0
quiz = {
    "Music": {
        "Question 1": {
            "question": "Who has the most Grammy wins? 1)Beyonce 2)Rihanna 3)Taylor Swift",
            "answer": "Beyonce"
        },
        "Question 2": {
            "question": "What album was the best-selling of all time? 1)ANTI 2)Lemonade 3)Thriller",
            "answer": "Thriller"
        },
        "Question 3": {
            "question": "What does VMA stand for? 1)Viral Music Awards 2)Video Music Awards 3)Various Music Awards",
            "answer": "Video Music Awards"
        },
        "Question 4": {
            "question":"What is the most valued award at the grammys? 1)Album Of The Year 2)Best New Artist 3)Song Of The Year",
            "answer":"Album of the year"
        }
    }
}

def is_letter(input_str):
    return input_str.isalpha()

def ask_questions(quiz,score):

    ask1 = input(quiz["Music"]["Question 1"]["question"])
    while True:
        if is_letter(ask1):
            answer1 = ask1.title()  
            if answer1 == quiz["Music"]["Question 1"]["answer"]:
                score = score + 1
                print("Correct! You have gained 1 point your score is now" ,score,)
            else:
                print("Incorrect your score is 1")
        else:
            print()


    

    ask2 = input(quiz["Music"]["Question 2"]["question"])
    answer2 = ask2.title()  
    if answer2 == quiz["Music"]["Question 2"]["answer"]:
        score = score + 1
        print("Correct! You have gained 1 point your score is now" ,score,)
    else:
        print("Incorrect your score is 1")

    ask3 = input(quiz["Music"]["Question 3"]["question"])
    answer3 = ask3.title()
    if answer3 == quiz["Music"]["Question 3"]["answer"]:
        score = score + 1
        print("Correct! You have gained 1 point your score is now" ,score,)
    else:
        print("Incorrect your score is 1")

    ask4 = input(quiz["Music"]["Question 4"]["question"])
    answer4 = ask4.title()
    if answer4 == quiz["Music"]["Question 4"]["answer"]:
        score = score + 1
        print("Correct! You have gained 1 point your score is now" ,score,)
    else:
        print("Incorrect your score is 1")

ask_questions(quiz,score,)