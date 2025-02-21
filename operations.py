# Calculation Operations

OPERATIONS_LIST = ["+", "-", "*", "/"]

def select_operators(operation: str, result: float, next_number: float) -> float:
    """
    This function for calculate numbers
    """
    if operation == OPERATIONS_LIST[0]:
        result += next_number
    elif operation == OPERATIONS_LIST[1]:
        result -= next_number
    elif operation == OPERATIONS_LIST[2]:
        result *= next_number    
    elif operation == OPERATIONS_LIST[3]:
        try:
            result /= next_number
        except ZeroDivisionError:
            return "Error: ZeroDivisionError."
    else:
        return "Selected operation is unavailable."
    return result