# Basic Quiz App (MCQ)
# To add questions, refer to the format in the data.json file found in the same directory as this file.
# JSON file format: {"q": question, "c": choices, "a": correct choice}

import json

# JSON file handler
with open("data.json", "r") as file:
    content = file.read()

data = json.loads(content)


score = 0

# Question iterator
for question in data:
    print(question["q"])
    for index, choice in enumerate(question["c"]):
        print(index+1, "-", choice)

    answer = input("Answer: ")
    if int(answer) == question["a"]:
        score = score + 1
        question["u"] = int(answer)
    else:
        question["u"] = int(answer)



for index, question in enumerate(data):
    try:
        user_answer = question["c"][question["u"] - 1]
    except:
        user_answer = "Invalid"
    correct_answer = question["c"][question["a"] - 1]
    message = f"{index + 1} - Your answer: {user_answer}, Correct answer: {correct_answer}."
    print(message)


print(f"Final score: {score}/{len(data)}")
if score == 2:
    print("Well done!")
else:
    print("Better luck next time.")