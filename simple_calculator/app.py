""" 
    Simple Calculator using Python

Author : Sahil Uddin Ishmam
Department : CSE
University : Metropolitan University

"""


# function definition

def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    try :
        return a/b
    except Exception as error:
        return error

def modulus(a,b):
    try :
        return a % b 
    except Exception as error:
        return error


# Main function
if __name__ == '__main__':
    while(True):

        print("---------------------------------------")

        # Implementation of user input handling

        print("""\n     Select operation :\n
                 1. Addition
                 2. Subtraction
                 3. Multiplication
                 4. Division
                 5. Modulus
                 6. Quit
              """)

