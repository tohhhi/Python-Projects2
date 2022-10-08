# dictionary that stores questions and answers
# have a variable that tracks the score of the player
# loop throw the dictionary using key value pairs
# display each question to the user and allow them to answer
# tell them if they are right or wrong
# show the final score when the quiz is finally completed



quiz = {
    "question1": {
        "question":"What is the capital of France?",
        "answer":"Paris"
    },
    "question2":{
        "question":"What is the capital of Germany?",
        "answer":"Berlin"
    },
    "question3":{
        "question":"What is the capital of Italy?",
        "answer":"Rome"
    },
    "question4":{
        "question":"What is the capital of Spain?",
        "answer":"Madrid"
    },
    "question5":{
        "question":"What is the capital of Portugal?",
        "answer":"Lisbon"
    },
    "question6":{
        "question":"What is the capital of Switzerland?",
        "answer":"Bern"
    },
    "question7":{
        "question":"What is the capital of Austria?",
        "answer":"Viena"
    },
    "question8":{
        "question":"What is the capital of Romania?",
        "answer":"Bucharest"
    }
}

score = 0

for k,v in quiz.items():
    print(v["question"])
    answer = input("Answer? ")
    
    if answer.lower() == v["answer"].lower():
        print("Correct")
        score = score + 1
        print("")
    else:
        print("Wrong")
        print("")
    
    
print(f"Congrats! Your score is: {score}")
print(f"Your percentage is: {score / 8 * 100}%.")