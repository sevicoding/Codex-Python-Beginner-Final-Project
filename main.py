from quiz import student_menu
from teacher import teacher_menu
from database import create_tables

def main():
    create_tables()  # ensure database tables exist

    while True:  # main loop
        print("\n=== ESL Vocabulary Trainer ===")
        print("Are you a (1) Student, (2) Teacher, or (3) Exit?")
        role = input("> ")

        if role == "1":
            student_menu()
        elif role == "2":
            teacher_menu()
        elif role == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
