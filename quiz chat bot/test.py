# useless_texts = ["um", "uh", "hmm", "sorry","never mind",
#                  "1","2","3","4","5","6","7","8","9",
#                  "10","11","12","13","14","15","16","17",
#                  "18","19","sqdqdeq"]

# user_input = input()

# if user_input.lower() in useless_texts:
#     print("I didn't get you. Can you please try again?")
# else:
#     print(f"{user_input}")
import random

# List of 5 MCQ questions with answers
mcq_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["New York", "London", "Paris", "Berlin"],
        "answer": "Paris"
    },
    {
        "question": "Who invented the telephone?",
        "options": ["Thomas Edison", "Alexander Graham Bell", "Guglielmo Marconi", "Nikola Tesla"],
        "answer": "Alexander Graham Bell"
    },
    {
        "question": "Which is the largest continent in the world?",
        "options": ["Africa", "Europe", "Asia", "South America"],
        "answer": "Asia"
    },
    {
        "question": "What is the largest organ in the human body?",
        "options": ["Brain", "Liver", "Heart", "Skin"],
        "answer": "Skin"
    },
    {
        "question": "Who wrote the Harry Potter series?",
        "options": ["J.K. Rowling", "Stephen King", "Dan Brown", "George R.R. Martin"],
        "answer": "J.K. Rowling"
    }
]

# Function to return 5 MCQ questions with answers
def get_mcq_questions():
    return random.sample(mcq_questions, 5)

# Test the function
user_input = input()
if user_input.lower() in ["provide me some mcq questions with answers","i want mcq questions","give me mcq questions", "mcq questions for reference"]:
    questions = get_mcq_questions()
    for i, question in enumerate(questions):
        print(f"\nQ{i+1}: {question['question']}")
        for j, option in enumerate(question['options']):
            print(f"   {chr(ord('a')+j)}. {option}")
        print(f"Answer: {question['answer']}")
# print()
# print("Do you need anytihng else ? ? ? ")
import random

def get_math_mcqs():
    math_mcqs = [
        {
            "question": "What is the value of pi (π)?",
            "options": ["3.14", "2.71", "1.62", "4.92"],
            "answer": "3.14"
        },
        {
            "question": "What is the square root of 81?",
            "options": ["9", "7", "6", "8"],
            "answer": "9"
        },
        {
            "question": "What is the value of 5 + 7?",
            "options": ["10", "11", "12", "13"],
            "answer": "12"
        },
        {
            "question": "What is the value of 8 * 4?",
            "options": ["32", "24", "40", "16"],
            "answer": "32"
        },
        {
            "question": "What is the value of 10 / 2?",
            "options": ["2", "3", "4", "5"],
            "answer": "5"
        }
    ]
    
    # Randomly select 5 MCQs from the list
    selected_mcqs = random.sample(math_mcqs, 5)
    
    # Create a formatted string with the selected MCQs and answers
    mcqs_with_answers = ""
    for i, mcq in enumerate(selected_mcqs):
        mcqs_with_answers += f"\n\nQ{i+1}. {mcq['question']}\n"
        for j, option in enumerate(mcq['options']):
            mcqs_with_answers += f"   ({j+1}) {option}\n"
        mcqs_with_answers += f"\n   Answer: {mcq['answer']}"
    
    return mcqs_with_answers



user_input = input()
if "mcq" in user_input.lower() and (" i want math mcq questions" in user_input.lower() or "math mcq questions please" or "i want math mcqs for reference" in user_input.lower()):
    math_mcqs = get_math_mcqs()
    print(math_mcqs)

