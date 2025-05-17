import random

# Sample question banks by subject and difficulty
QUESTION_BANK = {
    "math": {
        "easy": [
            ("What is 2 + 2?", "4"),
            ("What is 5 - 3?", "2"),
        ],
        "medium": [
            ("What is 12 x 3?", "36"),
            ("What is 144 ÷ 12?", "12"),
        ],
        "hard": [
            ("What is the square root of 169?", "13"),
            ("Solve: 2x + 3 = 11. What is x?", "4"),
        ]
    },
    "science": {
        "easy": [
            ("What planet do we live on?", "Earth"),
            ("What gas do humans need to breathe?", "Oxygen"),
        ],
        "medium": [
            ("What is H2O commonly known as?", "Water"),
            ("What organ pumps blood through the body?", "Heart"),
        ],
        "hard": [
            ("What is Newton's third law?", "Every action has an equal and opposite reaction"),
            ("What particle has a negative charge?", "Electron"),
        ]
    },
    "history": {
        "easy": [
            ("Who was the first President of the USA?", "George Washington"),
            ("What year did World War II end?", "1945"),
        ],
        "medium": [
            ("Who wrote the Declaration of Independence?", "Thomas Jefferson"),
            ("What empire was ruled by Julius Caesar?", "Roman Empire"),
        ],
        "hard": [
            ("What event started World War I?", "Assassination of Archduke Franz Ferdinand"),
            ("Who was the British Prime Minister during WWII?", "Winston Churchill"),
        ]
    }
}

def get_difficulty(age):
    if age <= 7:
        return "easy"
    elif 8 <= age <= 12:
        return "medium"
    else:
        return "hard"

def get_user_profile():
    print("🎓 Welcome to your personalized learning game!")
    name = input("What's your name? ")
    age = int(input("How old are you? "))
    subject = input("What subject do you want to learn? (math/science/history): ").lower()
    return {'name': name, 'age': age, 'subject': subject}

def generate_questions(subject, difficulty):
    questions = QUESTION_BANK.get(subject, {}).get(difficulty, [])
    return random.sample(questions, min(3, len(questions)))

def play_game(user):
    print(f"\n👋 Hi {user['name']}! Let's start your {user['subject'].capitalize()} quiz!")
    difficulty = get_difficulty(user['age'])
    questions = generate_questions(user['subject'], difficulty)

    score = 0
    for i, (question, answer) in enumerate(questions, 1):
        user_answer = input(f"Q{i}: {question} ")
        if user_answer.strip().lower() == answer.strip().lower():
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Oops! The correct answer was: {answer}\n")

    print(f"🎉 You got {score}/{len(questions)} correct. Great job, {user['name']}!")

def main():
    user = get_user_profile()
    play_game(user)

if __name__ == "__main__":
    main()
