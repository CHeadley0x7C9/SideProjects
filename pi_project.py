'''
Created a pi to n project using a decorator
'''
import math

#decorator logic
def pi_to_n(truncate):
	#first I will get a function using user input to provide me the decimal place the user choose
    def user_input():
        while True:
            try:
                d = int(input("Choose a decimal place from 1 - 16: "))
                if d in range(1,17):
                    print( truncate(d))
                    break
            except:
                print("sorry try again")
            else:
                continue
    return user_input()

@pi_to_n
# I created a function that will disple n numbers of decimal places
def truncate(decimals):
    multiplier = 10**decimals
    return int(math.pi*multiplier)/multiplier
