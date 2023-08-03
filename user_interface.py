import sys
#print(sys.path)
sys.path.append('.')
from classes.calculatorclass import calculator

def addtition(mycalculator):
    """
    Function to ask to the user the list of numbers to sum
    :param:mycalculator class to sum
    """
    while True:
        enter = input("Enter the numbers to sum devide by ',' : ")
        if enter == "":
            break
        numerossum = [int(num) for num in enter.split(",")]
        result = mycalculator.basic_operation_sum(*numerossum)
        return f"The addition is {result}"

def substraction(mycalculator):
    """
    Function to ask to the user the list of numbers to substract
    :param:mycalculator class to Substract
    """
    while True:
        enter = input("Enter the numbers to substract devide by ',' : ")
        if enter == "":
            break
        numerossum = [int(num) for num in enter.split(",")]
        result = mycalculator.basic_operation_sub(*numerossum)
        return f"The substraction is {result}"

def multiplication(mycalculator):
    """
    Function to ask to the user the list of numbers to multiply
    :param:mycalculator class to multiply
    """
    while True:
        enter = input("Enter the numbers to multiplication devide by ',' : ")
        if enter == "":
            break
        numerossum = [int(num) for num in enter.split(",")]
        result = mycalculator.basic_operation_mul(*numerossum)
        return f"The multiplication is {result}"

def divition(mycalculator):
    """
    Function to ask to the user the list of numbers to divide
    :param:mycalculator class to devide
    """
    while True:
        enter = input("Enter the numbers to devided devide by ',' : ")
        if enter == "":
            break
        numerossum = [int(num) for num in enter.split(",")]
        result = mycalculator.basic_operation_dev(*numerossum)
        return f"The divition is {result}"


if __name__ =="__main__":
    mycalculator = calculator()
    dic_op = {
        1: addtition,
        2: substraction,
        3: multiplication,
        4: divition
    }
    while True:
        print("==============Welcome============== \n Chosse one option :")
        print("1.- Addition")
        print("2.- Substraction")
        print("3.- Multiplication")
        print("4.- Divition")
        option = int(input("Enter a numerical option: "))
        print(dic_op[option](mycalculator))
