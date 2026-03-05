def user_info():
    # Collect name strings
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    try:
        age_input = input("Enter your age: ")
        age = int(age_input)

        if age < 0:
            print("Age cannot be negative")
        else:
            print("Full Name: " + first_name + " " + last_name)
            
            print(f"You will be {age + 1} next year")

    except ValueError:
        print("Invalid age input")

user_info()