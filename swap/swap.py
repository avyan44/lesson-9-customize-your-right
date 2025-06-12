def swap_three_digits():
    number = input("Enter a 3-digit number: ")

    
    if len(number) != 3 or not number.isdigit():
        print("Please enter a valid 3-digit number.")
        return

    a, b, c = number[0], number[1], number[2]
    print("Original:", a + b + c)
    print("Swap 1st and 2nd:", b + a + c)
    print("Swap 1st and 3rd:", c + b + a)
    print("Swap 2nd and 3rd:", a + c + b)
    print("Reverse all:", c + b + a)

swap_three_digits()
