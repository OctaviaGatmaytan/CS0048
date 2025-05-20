import sys

subject_list = []
score_list = []

def add_subject(subject):
    subject_list.append(subject)

def add_score(score):
    score_list.append(score)
    print(f"{score} has been added.")

def average():
    if score_list:
        return sum(score_list) / len(score_list)
    else:
        return None

while True:
    print("\n-- Menu --")
    print("1. Add Score")
    print("2. Calculate Average")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice (1-3): "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.")
        continue

    if choice == 1:
        subject = input("Enter subject: ")
        add_subject(subject)
        print(f"{subject} has been added.")
        try:
            score = float(input("Enter a score: "))
            add_score(score)
        except ValueError:
            print("Invalid score. Please enter a numeric value.")
    elif choice == 2:
        avg = average()
        if avg is not None:
            print(f"Average Grade: {avg:.2f}")
        else:
            print("No scores to calculate average.")
    elif choice == 3:
        print("Exiting... Goodbye!")
        sys.exit()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
