# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 08:49:00 2016

@author: bbarron

Number guessing game for Talk Python Class
"""
import random
print('------------------------------------')
print('           Guessing Game')

print('------------------------------------')
print('Welcome to the Guessing Game')
name = input('What is your name\n')
the_number = random.randint(0,100)
print ('The number is', the_number)
my_guess = -1

while my_guess != the_number:
  my_guess = input('Guess a number from 0 to 100, or "q" to quit\n')
  if my_guess in ["q","Q"]:
      exit('See you next time')
  guess = int(my_guess)
  #print guess
  if guess < the_number:
    print(str(my_guess)+ ' is Too low!')
  elif guess > the_number:
    print(str(my_guess)+ ' is too high!')
  else :
    print ('Fantastic, {} you guessed my number was {}'.format(name, guess))
    print()
    print()
    