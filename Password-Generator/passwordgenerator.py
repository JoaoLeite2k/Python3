import string
import random
import time
import os

LETTERS = string.ascii_letters
NUMBERS = '0123456789'
RANDOM = LETTERS + NUMBERS

count = 0
os.system('clear')
while count == 0:
    print('RANDOM P4$$W0RD GENERATOR')
    print('Enter the password lenght')
    lenght = int(input('>> '))
    password = ''.join(random.sample(RANDOM, lenght))
    time.sleep(2)
    os.system('clear')
    print('Generating the password...')
    time.sleep(1)
    os.system('clear')
    time.sleep(1)
    print('Generating the password...')
    time.sleep(1)
    os.system('clear')
    time.sleep(1)
    print('Your new password is: ' + password)
    
    time.sleep(3)
    print('Generate a new password?')
    print('1. Yes')
    print('2. No')
    choose = int(input('>> '))
    if choose == 2:
        print('Exiting...')
        count += 1
    os.system('clear')
    time.sleep(2)