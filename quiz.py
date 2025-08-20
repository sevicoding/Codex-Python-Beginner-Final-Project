import random
from database import connect

def student_menu():
    name = input("Enter your name: ")
    print(f"Welcome, {name}!\n")

    while True:  # student quiz loop
        run_quiz(name)
        cont = input("Do you want to answer another word? (y/n) ")
        if cont.lower() != "y":
            break

def run_quiz(student):
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT id, word, meaning, difficulty FROM words")
    words = c.fetchall()

    if not words:
        print("No words in database. Ask teacher to add some!\n")
        return

    # Pick a random word
    word = random.choice(words)
    word_id, eng, meaning, diff = word

    # Show the foreign meaning first
    print(f"\nWhat is the English word for '{meaning}'?")
    guess = input("> ")

    if guess.lower().strip() == eng.lower().strip():  # check English word
        print("✅ Correct!\n")
        c.execute("INSERT INTO scores (student, word_id, correct) VALUES (?, ?, 1)", (student, word_id))
        if diff > 1:
            c.execute("UPDATE words SET difficulty = difficulty - 1 WHERE id = ?", (word_id,))
    else:
        print(f"❌ Wrong! Correct answer: {eng}\n")
        c.execute("INSERT INTO scores (student, word_id, correct) VALUES (?, ?, 0)", (student, word_id))
        c.execute("UPDATE words SET difficulty = difficulty + 1 WHERE id = ?", (word_id,))

    conn.commit()
    conn.close()
