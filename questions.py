import json

with open('quetions.json', 'r') as file:
    content = file.read()

data = json.loads(content)

score = 0

for question in data:
    print(question['question_text'])
    for index, alternatives in enumerate(question['alternatives']):
        print(index + 1,'.', alternatives)
    user_choice = int(input("Enter your choice: "))
    question['user_choice'] = user_choice
    
    if question["user_choice"] == question['correct_answer']:
        score = score + 1
        result = "Correct answer!"
else:
    result = "Wrong answer!"

        

for index, question in enumerate(data):
    message = f"{result} {index + 1}. Your answer: {question["user_choice"]}, " \
              f"Correct answer: {question["correct_answer"]}"
    print(message)

print(data)
print(score)











