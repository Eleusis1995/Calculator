
from classes.calculatorclass import calculator


if __name__ =="__main__":
    mycalculator = calculator()

    while True:
        print("Welcome /n Chosse one option")
        print("1.- Suma")
        print("2.- Resta")
        print("3.- Mult")
        print("4.- Div")
        option = int(input("Enter a numerical option: "))
        if option == 1:
            while True:
                enter = input("Enter the numbers to sum devide by ',' : ")
                if enter == "":
                    break
                numerossum = [int(num) for num in enter.split(",")]

                result = mycalculator.basic_operation_sum(*numerossum)
                print(f"The addition is {result}")