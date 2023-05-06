def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')
    print('I was Designed & Developed by Aditya Pimpale')


def ask_name():
    print()
    print('Please, can you tell me your name ? ? ?')
    name = input()
    print('What a great name you have, ' + name + '!')
    print()

def ask_location():    
    location = input("From where do you belong: ")
    if location.lower() in ["pune","akurdi","mumbai","delhi","new york", "los angeles", "chicago"]:
      print()  
      print("Welcome to the big city!")
    elif location.lower() in ["miami","goa","dapoli","bahamas","konkan", "new orleans", "san diego"]:
        print()
        print("Enjoy the sun and beach!")
    else:
      print() 
      print("Never heard of it, I think I have to learn a lot about cities :|")
      print()
    


def guess_age():
    print()
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good to hear, may you live to your fullest potential in your future life!")
    

def count():
    print()
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def MCQ1():
    print('Now, as I am an Quiz Chat Bot')
    print('Lets start the General knowledge Quiz ') 
    print()
    print("Let's test your programming knowledge.")
    print("Which among the following languages is the slowest?")
    print("1. Java")
    print("2. C++")
    print("3. Python")
    while input() != '3':
        print('Please, try again.')
    print("Yes you are right")
    print()
     
def MCQ2():
    print("Now let's test your mathematical knowledge.")
    print("What is the square root of 121?")
    print("1. 11")
    print("2. 12")
    print("3. 32")
    while input() != '1':
        print('Please, try again.')
    print("Ok !!")
    print("Your math looks fine to me!")
    print()
    
def MCQ3():
    print("Lets see how truly good is your logic ")
    print()
    print("def mystery(n): \n if n == 1: \n return 1 \n elif n % 2 == 0: \n return mystery(n/2) + 1 \n  else: \n return mystery(3*n+1) + 1")
    print()
    print("What does the mystery(n) function do?")
    print("1. Calculates the factorial of n")
    print("2. Calculates the sum of the first n natural numbers")
    print("3. Calculates the length of the Collatz sequence starting from n")
    print("4. Calculates the nth Fibonacci number")
    while input() != '3':
        print('Please, try again.')
    print("Wow you have great programming logic :D  !!")
    print("Sorry to underestimate you :( ")
    
import random
def MCQ4():
# Generate two random numbers between 1 and 10
 num1 = random.randint(1, 10)
 num2 = random.randint(1, 10)

# Create a math question by combining the two numbers with an operator
 operator = random.choice(["+", "-", "*"])
 question = f"What is {num1} {operator} {num2}? "

# Get the user's answer
 answer = input(question)
 
# Calculate the correct answer
 if operator == "+":
    correct_answer = num1 + num2
 elif operator == "-":
    correct_answer = num1 - num2
 else:
    correct_answer = num1 * num2

# Check if the user's answer is correct and print a message
 if int(answer) == correct_answer:
    print("Correct!")
 else:
    print(f"Sorry, the correct answer is {correct_answer}.")




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
def ask_mcq_questions():
 user_input = input()
 if user_input.lower() in ["provide me some mcq questions with answers","i want mcq questions","give me mcq questions", "mcq questions for reference"]:
    questions = get_mcq_questions()
    for i, question in enumerate(questions):
        print(f"\nQ{i+1}: {question['question']}")
        for j, option in enumerate(question['options']):
            print(f"   {chr(ord('a')+j)}. {option}")
        print(f"Answer: {question['answer']}")

def end():
    print()
    print("Thank you for playing!")
    print()
    print("Hope the quiz and the mcq, that I've provided were good enough")
    print()
    print("Have a nice day!")

greet('Quiz Genie', '2023')
ask_name()
ask_location()
guess_age()
count()
MCQ1()
MCQ2()
MCQ3()
MCQ4()
ask_mcq_questions()
end()
