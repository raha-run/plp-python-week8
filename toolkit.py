
print("Welcome to Raha's Personal Mini-Toolkit!")

tasks = []

while True:
    print("\nPlease choose a tool:")
    print("1. Simple Calculator")
    print("2. To-Do List")
    print("3. Even Number Checker")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Simple calculator adds two numbers.
        print("\n--- Simple Calculator ---")

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = num1 + num2

        print(f"{num1} + {num2} = {result}")

    elif choice == "2":
        # To-Do List stores tasks in a list.
        print("\n--- To-Do List ---")

        task = input("Enter a task: ")
        tasks.append(task)

        print(f"Task added: {task}")
        print(f"Your tasks: {tasks}")

    elif choice == "3":
        # Even Number Checker decides whether a number is even or odd.
        print("\n--- Even Number Checker ---")

        number = int(input("Enter a number: "))

        if number % 2 == 0:
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")

    elif choice == "4":
        print("Goodbye! Thanks for using Raha's Mini-Toolkit.")
        break

    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")

