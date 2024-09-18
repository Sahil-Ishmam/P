import random

"""
Simple Number Guessing Game

Author : Sahil Uddin Ishmam
Department : CSE
University : Computer science and Engineering

"""




if __name__ == '__main__':
    
    run = True
    while(run):
        print("""
                Welcome to the Number Guessing Game!
                Try to guess the number between 1 and 100
            
            """)
        # Generating random number between 1 to 100
        secret_number = random.randint(1,100)
        count_attempt = 0

        while(True):
            # Taking user guess
            user_number = input("Enter your guess: ")

            try:
                user_number = int(user_number)
            except Exception as error:
                print(error)
                continue

            count_attempt += 1
            

            if user_number == secret_number :
                print(f"Congratulations! You've guessed the number in {count_attempt} attempts.")
                break
            elif user_number > secret_number :
                print("Too high!")
            elif user_number < secret_number :
                print("Too low!")
    
        con = input("Do you want to play this again ? YES/NO : ").lower()
        yes_words = ['yes','yeah','yup','yah','1','y']
        no_words = ['no','nope','not','0',"n"]
        if con in yes_words :
            run = True
        elif con in no_words :
            run = False
            print("Programme Terminated!!")
        
    

            


    
    


