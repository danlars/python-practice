# Install PyMySQL --------- pip3 install PyMySQL
from hangman.modules.TheGame import hangmanTheGame as hangman

#TODO: get number of characters from string and insert as _ in console
#TODO: After each guess, if correct, remove _ and replace with the guessed character at each respective character placement
#TODO: Maximum of 10 guesses (vi kan altid lave det om)
#TODO: Funsies, draw a hangman in console

print("Hello and welcome to the hangman game, what's your name?")
name = input('insert name: ')

if not name:
    name = "guest"

hangman(name)

print("Exited program")