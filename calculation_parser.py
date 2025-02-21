from operations import OPERATIONS_LIST, select_operators

def calculate_expression(expression):
    number = ""
    operators = []
    numbers = []
    
    expression = expression.replace(" ", "")
    
    for char in expression:
        if char.isdigit() or char == ".":
            number += char
        else:
            if number:
                numbers.append(float(number))
                number = ""
            if char in OPERATIONS_LIST:
                operators.append(char)
            else:
                print(f"Invalid operator: {char}")
                return None
    
    if number:
        numbers.append(float(number))
    
    if not numbers or len(numbers) - 1 != len(operators):
        print("Invalid expression format")
        return None

    result = numbers[0]
    for i, operator in enumerate(operators):
        result = select_operators(operator, result, numbers[i + 1])
    
    return result

expression = input("Enter your mathematical expression >> ")
result = calculate_expression(expression)

if result is not None:
    print(f"Result is {result}")