# menu function

def main_menu():
    print()
    # Welcome message
    print("\t\t**** Welcome to the Dashboard ****")
    print("\t\t*** ENTER A MENU CHOICE NUMBER ***")
    print()
    # Options for the user to choose from
    print('1) Beginner: Hello basic')
    print('2) Intermediate: Numbers Basic')
    print('3) Intermediate: Numbers Value Check')
    print('4) Intermediate: Numbers Range Check')
    print('5) Intermediate: Average of 3 Numbers')
    print('6) Intermediate: Highest Entered Number')
    print('7) Intermediate: Even number count')
    print('8) Advanced: Powers Function')
    print('9) Advanced: Powers to max entered number')
    print('99) Exit the program')
    # return the user's choice
    choice = int(input("\n  Enter a menu number: "))
    return choice


"""
Menu Option 1. Beginner: Hello basic
"""


def menu_option_1():
    forename = input("Enter your first name: ")
    print("Hello", forename)


"""
Menu Option 2. Intermediate: Numbers basic
"""


def menu_option_2():
    # set up an empty list to store the numbers entered
    numbers_entered = []
    print("You are going to be asked to enter 3 integer numbers. Enter them at the prompt.")
    print(" ")
    num1 = int(input("Enter the first number: "))
    numbers_entered.append(num1)
    num2 = int(input("Enter the second number: "))
    numbers_entered.append(num2)
    num3 = int(input("Enter the third number: "))
    numbers_entered.append(num3)
    print(" ")
    print("The numbers you entered are: ", numbers_entered)


"""
Menu Option 3. Intermediate: Numbers Value Check
"""


def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        print("That\'s not an integer value. Please try again.")
        print("")
        return False


def menu_option_3():
    # set up an empty list to store the numbers entered
    numbers_entered = []
    print("You are going to be asked to enter 3 integer numbers. Enter them at the prompt.")
    print(" ")
    num1 = input("Enter the first number: ")
    while is_integer(num1) == False:
        print("Please enter an integer value")
        num1 = input("Enter the first number: ")
    numbers_entered.append(num1)
    num2 = input("Enter the second number: ")
    while is_integer(num2) == False:
        print("Please enter an integer value")
        num2 = input("Enter the second number: ")
    numbers_entered.append(num2)
    num3 = input("Enter the third number: ")
    while is_integer(num3) == False:
        print("Please enter an integer value")
        num3 = input("Enter the third number: ")
    numbers_entered.append(num3)
    print(" ")
    print("The numbers you entered are: ", numbers_entered)


"""
Menu Option 4. Intermediate: Numbers range check
"""


# First check if the number is less than 20
def is_valid(num):
    """Check if the number is less than 20."""
    return num < 20


# Combined function to check if the input is an integer and less than 12
def is_integer_and_valid(user_input):
    try:
        # Attempt to convert the input to an integer
        converted_number = int(user_input)
        # Check if the converted number is less than 12
        if is_valid(converted_number):
            return True  # Return True if the number is also less than 12
        else:
            print("The number must be less than 20, try again")
            return False  # Return False if the number is 12 or greater
    except ValueError:
        # A ValueError occurs if the conversion fails
        print("The number entered is not an integer, try again")
        return False  # Return False if the input is not an integer


# Bringing it together in the menu option
def menu_option_4():
    # set up an empty list to store the numbers entered
    numbers_entered = []
    print("You are going to be asked to enter 3 integer numbers. Enter them at the prompt.")
    print("Each number must be less than 20")
    print(" ")
    num1 = input("Enter the first number: ")
    while not is_integer_and_valid(num1):
        print("Please enter an integer value")
        num1 = input("Enter the first number: ")
    numbers_entered.append(num1)
    num2 = input("Enter the second number: ")
    while not is_integer_and_valid(num2):
        print("Please enter an integer value")
        num2 = input("Enter the second number: ")
    numbers_entered.append(num2)
    num3 = input("Enter the third number: ")
    while not is_integer_and_valid(num3):
        print("Please enter an integer value")
        num3 = input("Enter the third number: ")
    numbers_entered.append(num3)
    print(" ")
    print("The numbers you entered are: ", numbers_entered)


"""
Menu Option 5. Intermediate: Average of 3 Numbers
"""


# We can reuse the functions we created for menu-option-4
def menu_option_5():
    # set up an empty list to store the numbers entered
    numbers_entered = []
    # set up a variable to store the total of the numbers entered
    numbers_total = 0

    print("You are going to be asked to enter 3 integer numbers. Enter them at the prompt.")
    print("Each number must be less than 20")
    print(" ")
    num1 = input("Enter the first number: ")
    while not is_integer_and_valid(num1):
        print("Please enter an integer value")
        num1 = input("Enter the first number: ")
    numbers_entered.append(num1)
    numbers_total += int(num1)
    num2 = input("Enter the second number: ")
    while not is_integer_and_valid(num2):
        print("Please enter an integer value")
        num2 = input("Enter the second number: ")
    numbers_entered.append(num2)
    numbers_total += int(num2)
    num3 = input("Enter the third number: ")
    while not is_integer_and_valid(num3):
        print("Please enter an integer value")
        num3 = input("Enter the third number: ")
    numbers_entered.append(num3)
    numbers_total += int(num3)
    print(" ")
    print("The numbers you entered are: ", numbers_entered)
    print("The average of the numbers entered is: ", numbers_total / 3)
    # print("The average of the numbers entered is: ", sum(numbers_entered) / len(numbers_entered))


"""
Menu_option_6 - Intermediate: Highest number entered
"""


def menu_option_6():
    # set up an empty list to store the numbers entered
    numbers_entered = []
    print("You are going to be asked to enter 3 integer numbers. Enter them at the prompt.")
    print(" ")
    num1 = input("Enter the first number: ")
    while not is_integer_and_valid(num1):
        print("Please enter an integer value")
        num1 = input("Enter the first number: ")
    numbers_entered.append(num1)
    num2 = input("Enter the second number: ")
    while not is_integer_and_valid(num2):
        print("Please enter an integer value")
        num2 = input("Enter the second number: ")
    numbers_entered.append(num2)
    num3 = input("Enter the third number: ")
    while not is_integer_and_valid(num3):
        print("Please enter an integer value")
        num3 = input("Enter the third number: ")
    numbers_entered.append(num3)
    print(" ")
    print("The numbers you entered are: ", numbers_entered)
    # We can use a built-in method that works for Python lists to find the highest number
    print("The highest number entered is: ", max(numbers_entered))


"""
Menu_option_7 - Intermediate: Even number count
"""


def menu_option_7():
    # set up an empty list to store the numbers entered
    numbers_entered = []
    print("You are going to be asked to enter 3 integer numbers. Enter them at the prompt.")
    print(" ")
    num1 = input("Enter the first number: ")
    while not is_integer_and_valid(num1):
        print("Please enter an integer value")
        num1 = input("Enter the first number: ")
    numbers_entered.append(num1)
    num2 = input("Enter the second number: ")
    while not is_integer_and_valid(num2):
        print("Please enter an integer value")
        num2 = input("Enter the second number: ")
    numbers_entered.append(num2)
    num3 = input("Enter the third number: ")
    while not is_integer_and_valid(num3):
        print("Please enter an integer value")
        num3 = input("Enter the third number: ")
    numbers_entered.append(num3)
    print(" ")
    print("The numbers you entered are: ", numbers_entered)
    # We can go through the list and count the even numbers
    even_count = 0

    for number in numbers_entered:
        if int(number) % 2 == 0:
            even_count += 1
    print("The number of even numbers entered is: ", even_count)
    # A different way to print the result
    print(f"{even_count} even numbers were entered.")







"""
Menu_option_8 - Advanced: Powers function
"""

def power(base,exponent):
    # Validate input types - they must be integers
    if not isinstance(base, int) or not isinstance(exponent, int):
        raise ValueError("Both base and exponent must be integers.")

    return base ** exponent

def menu_option_8():
    print(" ")
    print("You have selected the Advanced: Powers Function")
    print(" ")
    # Get the base and exponent from the user
    base = int(input("Enter the base number: "))
    exponent = int(input("Enter the exponent: "))
    # Call the power function and print the result
    print(f"The result of {base} to the power of {exponent} is: {power(base, exponent)}")


"""
Menu_option_9 - Advanced: Powers to max entered number
"""
def powers_range(base, exponent):
    # Validate input types and the value of the exponent
    if not isinstance(base, int) or not isinstance(exponent, int):
        raise ValueError("Both base and exponent must be integers.")
    if exponent > 9:
        raise ValueError("Exponent must be 9 or less.")

    # Iterate over the range from 1 to the exponent inclusive
    for power in range(1, exponent + 1):
        result = base ** power
        print(f"{base} raised to the power of {power} is: {result}")

def menu_option_9():
    print(" ")
    print("You have selected the Advanced: Powers to max entered number")
    print("The power you want to raise to must be less than 10")
    print(" ")
    # Get the base and exponent from the user
    base = int(input("Enter the base number: "))
    exponent = int(input("Enter the exponent. It must be 9 or less: "))
    # Call the power function and print the result
    print(f"The results of {base} to the power of 1 to {exponent} are: {powers_range(base, exponent)}")


# *****************************************************************
# *****************************************************************
# MENU Implementation
# *****************************************************************
# Display menu when application launches
x = main_menu()

while x == 1 or x == 2 or x == 3 or x == 4 or x == 5 or x == 6 or x == 7 or x == 8 or x == 9 or x == 99:
    if x == 1:
        print(" ")
        print("You have selected the Beginner: Hello basic")
        menu_option_1()
    elif x == 2:
        print("You have selected the Intermediate: Numbers Basic")
        menu_option_2()
    elif x == 3:
        print(" ")
        print("You have selected the Intermediate: Numbers Value Check")
        menu_option_3()
    elif x == 4:
        print(" ")
        print("You have selected the Intermediate: Numbers Range Check")
        menu_option_4()
    elif x == 5:
        print(" ")
        print("You have selected the Intermediate: Average of 3 Numbers")
        menu_option_5()
    elif x == 6:
        print(" ")
        print("You have selected the Intermediate: Highest number entered")
        menu_option_6()
    elif x == 7:
        print(" ")
        print("You have selected the Intermediate: Even number count")
        menu_option_7()
    elif x == 8:
        print(" ")
        print("You have selected the Advanced: Powers Function")
        menu_option_8()
    elif x == 9:
        print(" ")
        print("You have selected the Advanced: Powers to max entered number")
        menu_option_9()
    elif x == 99:
        print(" ")
        print("You have selected to Exit the program")
        break

    x = main_menu()
