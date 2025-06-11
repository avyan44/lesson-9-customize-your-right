def check_year_10_eligibility():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    if age < 10:
        print(f"Sorry {name}, you can't join Year 10.")
    else:
        print(f"Welcome {name}, you're eligible to join Year 10!")

# Run the function
check_year_10_eligibility()

