#Ask user on what Operation to do
#define addition operation
def add():
    #ask user for the first number
    number_1_input = float(input("What is the first number? "))
    #ask the user for seconnd number
    number_2_input = float(input("What id your second number? "))
    #try to run the numbers in the code if the type is correct
    try:
        number_output = number_1_input + number_2_input
        print(str(number_output))
    except ValueError:
        print("That is a string please input an integer")
#
#define subtraction operation
def subtract():
    #ask user for the first number
    number_1_input = float(input("What is yur first number? "))
    #ask the user for seconnd number
    number_2_input = float(input("What is yur second number? "))
    #try to run the numbers in the code if the type is correct
    try:
        number_output = number_1_input - number_2_input
        print(str(number_output))
    except ValueError:
        print("That is a string please input an integer")
#
#define multiplication operation
def multiply():
    #ask user for the first number
    number_1_input = float(input("What is yur first number? "))
    #ask the user for seconnd number
    number_2_input = float(input("What is yur second number? "))
    #try to run the numbers in the code if the type is correct
    try:
        number_output = number_1_input * number_2_input
        print(str(number_output))
    except ValueError:
        print("That is a string please input an integer")
#
#define division operation
def divide():
    #ask user for the first number
    number_1_input = float(input("What is yur first number? "))
    #ask the user for seconnd number
    number_2_input = float(input("What is yur second number? "))
    #try to run the numbers in the code if the type is correct and if it will be a zero division error
    try:
        number_output = number_1_input / number_2_input
        print(str(number_output))
    except ValueError:
        print("That is a string please input an integer")
    except ZeroDivisionError:
        print("The number is being divided by a zero")
#
#