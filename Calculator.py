def addition(num1, num2):
    return num1 + num2
 
def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2
 
def modules(num1, num2):
    return num1 % num2
 
def exponentiation(num1, num2):
    return num1 ** num2
 
def floordivision(num1, num2):
    return num1 // num2

while True:
     print("\n Operations on the calculator \n 1. Addition\n 2. Subtraction\n 3. Multiplication \n 4. Division\n 5. Modules\n 6. Exponentiation\n 7. Floor Division\n")
     op = int(input("Enter your Operation:"))
     number_1= int(input("Enter the first number: "))
     number_2 = int(input("Enter the second number: "))
 
     if op == 1:
         print(number_1, "+", number_2, "=",
                    addition(number_1, number_2))
     elif op == 2:
         print(number_1, "-", number_2, "=",
                    subtraction(number_1, number_2))
     elif op == 3:
         print(number_1, "*", number_2, "=",
                    multiplication(number_1, number_2))
     elif op == 4:
         print(number_1, "/", number_2, "=",
                    division(number_1, number_2))
     elif op == 5:
         print(number_1, "%", number_2, "=",
                    modules (number_1,number_2))
     elif op == 6:
         print(number_1, "**", number_2, "=",
                    exponentiation(number_1, number_2))
     elif op == 7:
         print(number_1, "//", number_2, "=",
                    floordivision(number_1, number_2))
     else:
         print("Invalid input")
         break