while True:
    #define addition operation
    def add():
        #ask user for the first number
        print("\033[1;32m ` \n")
        number_1_input = float(input("What is the first number? "))
        #ask the user for seconnd number
        number_2_input = float(input("What id your second number? "))
        #try to run the numbers in the code if the type is correct
        try:
            number_output = number_1_input + number_2_input
            print("\n" + str(number_output) + "\n")
        except ValueError:
            print("That is a string please input an integer")
    #
    #define subtraction operation
    def subtract():
        #ask user for the first number
        print("\033[1;32m ` \n")
        number_1_input = float(input("What is yur first number? "))
        #ask the user for seconnd number
        number_2_input = float(input("What is yur second number? "))
        #try to run the numbers in the code if the type is correct
        try:
            number_output = number_1_input - number_2_input
            print("\n" + str(number_output) + "\n")
        except ValueError:
            print("That is a string please input an integer")        
    #
    #define multiplication operation
    def multiply():
        #ask user for the first number
        print("\033[1;32m ` \n")
        number_1_input = float(input("What is yur first number? "))
        #ask the user for seconnd number
        number_2_input = float(input("What is yur second number? "))
        #try to run the numbers in the code if the type is correct
        try:
            number_output = number_1_input * number_2_input
            print("\n" + str(number_output) + "\n")
        except ValueError:
            print("That is a string please input an integer")          
    #
    #define division operation
    def divide():
        #ask user for the first number
        print("\033[1;32m ` \n")
        number_1_input = float(input("What is yur first number? "))
        #ask the user for seconnd number
        number_2_input = float(input("What is yur second number? "))
        #try to run the numbers in the code if the type is correct and if it will be a zero division error
        try:
            number_output = number_1_input / number_2_input
            print("\n" + str(number_output) + "\n")
        except ValueError:
            print("That is a string please input an integer")
        except ZeroDivisionError:
            print("The number is being divided by a zero")

    addition_input_list = ["add" , "Add" , "ADD" , "addition","Addition" , "ADDITION"]
    subtraction_input_list = ["minus" , "Minus", "MINUS" , "subtract" , "Subtraction" , "SUBTRACTION"]
    division_input_list = ["divide", "Divide", "DIVIDE", "division" , "Division", "DIVISION"]
    multiplication_input_list = ["multiply", "Multiply", "MULTIPLY", "multiplication", "Multiplication", "MULTIPLICATION"]

    #Ask user on what Operation to do
    print("\033[1;32m ` \n")
    print("Welcome to my Calculator na pinacomplicated\n\nIkaw ba ay mag:\n\nAddition\nSubtraction\nMultiplication\nDivision\n")
    operation_user_input = str(input("What Operation would you like to use?: "))

    if operation_user_input in addition_input_list:
        add()
    elif operation_user_input in subtraction_input_list:
        subtract()
    elif operation_user_input in multiplication_input_list:
        multiply()
    elif operation_user_input in division_input_list:
        divide()
    else:
        print("Please input the right operation :)")
    try_again = input("Would you like to calculate again?:")
    print("\n")
    yes_user_input = ["Y" , "y" , "Yes" , "YES"]
    no_user_input =["N", "n" , "No" , "NO"]
    if try_again in yes_user_input:
        continue
    elif try_again in no_user_input:
        break