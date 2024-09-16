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
    pass

