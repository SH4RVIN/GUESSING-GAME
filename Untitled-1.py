def game_quiz():
    questions = [
        {
            "question": "what game has a best strategy award in Roblox?",
            "choices": ["Tag game", "The Dusty Trip", "TDS", "TSB"],
            "answer": "TDS"
        },
        {
            "question": "Which game is known for the phrase 'The cake is a lie'?",
            "choices": ["Portal", "Half-Life", "Fall Guys", "Super Mario Bros"],
            "answer": "Portal"
        },
        {
            "question": "Which game features a 32 player multiplayer battle royale ?",
            "choices": ["Stumble Guys", "Fall Guys", "War Robots", "Overwatch"],
            "answer": "Stumble Guys"
        },
        {
            "question": "Which game that gives infinite creativity?",
            "choices": ["Halo", "Minecraft", "Sandbox", "Souls"],
            "answer": "Minecraft"
        },
        {
            "question": "Which game is the Most Famous in Roblox?",
            "choices": ["Brookhaven", "Livetopia", "Blade Ball", "Adopt Me"],
            "answer": "Brookhaven"
        }
    ]

    print("Welcome to the Game Quiz!")
    score = 0

    for q in questions:
        print("\n" + q["question"])
        for i, choice in enumerate(q["choices"], 1):
            print(f"{i}. {choice}")

        try:
            answer = int(input("Enter the number of your answer: "))
            if q["choices"][answer - 1] == q["answer"]:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {q['answer']}")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number corresponding to the choices.")

    print(f"\nYou answered {score} out of {len(questions)} questions correctly.")

if __name__ == "__main__":
    game_quiz()
