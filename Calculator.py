# The code for a calculator that takes user inputs and perform arithmetic operations until the user press '='
def Calculator(): 
    operators = ['+', '-', '*', '/', '^']
    currentOperator = None
    result = None

    while True:
        # Taking the input from the user , this can be a number or an operator
        userInput = input()

        # The stopping condition
        if userInput == '=':
            break

        #  if the user enters an operator
        if userInput in operators:
            currentOperator = userInput
        else :
            # means the user enters a number
            number = float(userInput)
            if result is None:
                result = number
            else :
                if currentOperator == '+':
                    result += number
                elif currentOperator == '-':
                    result -= number
                elif currentOperator == '*':
                    result *= number
                elif currentOperator == '/':
                    if number != 0:
                       result /= number
                    else:
                       print("Division by zero not possible ! ")
                elif currentOperator == '^':
                    result **= number
                else:
                    print("Operation cant be performed !")

    if result != None:
        print(result)
    else :
        print("Caclculation not performed !")

Calculator()
