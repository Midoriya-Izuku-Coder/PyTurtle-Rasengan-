#Hour of Code HK - animal quiz
#Author: Caliabc
#Date: Feb 7, 2021
def check_guess(guess,answer):
    if guess == answer:
        print('correct answer')
    else:
        print('wrong answer')
    
print('HoCHK')
print('Guess the animal')
#print(input('Which kind of bears live in the north pole?'))
guess = input("Which bear live in the north pole?')
print(guess)
answer = 'polar bear'
