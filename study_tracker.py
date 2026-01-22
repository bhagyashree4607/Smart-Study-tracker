study_log = []

while True:
    print("\n1. Add Study Entry")
    print("2. View Study Log")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        subject = input("Subject: ")
        hours = input("Hours studied: ")
        study_log.append((subject, hours))
        print("Entry added!")

    elif choice == "2":
        if not study_log:
            print("No study data available.")
        else:
            for i, entry in enumerate(study_log, start=1):
                print(f"{i}. Subject: {entry[0]}, Hours: {entry[1]}")

    elif choice == "3":
        print("Good luck with your studies!")
        break

    else:
        print("Invalid choice.")
