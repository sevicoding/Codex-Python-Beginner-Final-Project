from database import connect

def teacher_menu():
    while True:
        print("\n=== Teacher Menu ===")
        print("1. Add new word")
        print("2. Show top 5 hardest words")
        print("3. Show all words")
        print("4. Clear all words")      # <- new option
        print("5. Return to main menu")
        choice = input("> ")

        if choice == "1":
            add_word()
        elif choice == "2":
            show_reports()
        elif choice == "3":
            show_word_list()
        elif choice == "4":
            clear_words()
        elif choice == "5":
            break
        else:
            print("Invalid choice.\n")


def add_word():
    conn = connect()
    c = conn.cursor()
    word = input("Enter English word: ")
    meaning = input("Enter meaning/translation: ")
    c.execute("INSERT INTO words (word, meaning) VALUES (?, ?)", (word, meaning))
    conn.commit()
    conn.close()
    print(f"✅ Added {word}")

def show_reports():
    conn = connect()
    c = conn.cursor()
    c.execute("""
        SELECT w.word, SUM(CASE WHEN s.correct=0 THEN 1 ELSE 0 END) as wrongs
        FROM scores s
        JOIN words w ON s.word_id = w.id
        GROUP BY w.word
        ORDER BY wrongs DESC
        LIMIT 5
    """)
    results = c.fetchall()
    print("\nTop 5 hardest words:")
    for word, wrongs in results:
        print(f"{word}: {wrongs} mistakes")
    conn.close()

def show_word_list():
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT id, word, meaning, difficulty FROM words")
    words = c.fetchall()
    conn.close()

    if not words:
        print("No words in the database yet.\n")
        return

    print("\n=== Word List ===")
    for w_id, word, meaning, diff in words:
        print(f"{w_id}. {word} → {meaning} (difficulty: {diff})")
    print()
    conn.close()

def clear_words():
    confirm = input("Are you sure you want to delete ALL words? (y/n): ")
    if confirm.lower() == "y":
        conn = connect()
        c = conn.cursor()
        c.execute("DELETE FROM words")  # removes all words
        c.execute("DELETE FROM scores") # optional: clear scores too
        conn.commit()
        conn.close()
        print("✅ All words (and scores) have been deleted.\n")
    else:
        print("Operation cancelled.\n")