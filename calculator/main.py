def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return  number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    if number2 == 0:
        return "Error: Division by zero is not allowed."
    else:
        return number1 / number2
    

print("You can only select any one opraction at a time : -\n" 
        "1. Addition\n" \
        "2. Subtraction\n" \
        "3. Multiplication\n" \
        "4. Division\n")

user_input = int(input("Enter your opraction number: "))
if user_input > 4:
    print("Invalid input. Please select a number between 1 and 4. -\n" "Refresh the dialog")


number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))

if user_input == 1:
    print(f"{number1} + {number2} = {add(number1, number2)}")


elif user_input == 2:
    print(f"{number1} - {number2} = {subtract(number1, number2)}")


elif user_input == 3:
    print(f"{number1} * {number2} = {multiply(number1, number2)}")


elif user_input == 4:
    print(divide(number1, number2))


else:
    print("Invalid input. Please try again.")