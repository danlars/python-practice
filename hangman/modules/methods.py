
def character_guess(word, guessedCharacters):#Create underscore characters for each existing letter in word
    characters = ""
    for x in word:
        if str(x).lower() in str(guessedCharacters).lower() or x == " ":
            characters += x
        else:
            characters += "_"
    return characters

def MySQLWords(ar): #MySQL words that are not to be repeated
    count = 0
    stringArrays = ""

    for row in ar:
        if count == 0:
            count = 1
            stringArrays += '\'{}\''.format(row)
        else:
            stringArrays += ',\'{}\''.format(row)

    return stringArrays

def checkCharacter(guessedCharacter, guessedCharacters): #Check if guessed character is legal
    illegalCharacters = \
        [',', ';', '.', ':', '-', '_', '!', '"', '@', '#', '£', '¤', '$', '§', '½', '¾', '%', '&', '¥', '/', '{', '(', '[', ')', ']', '=', '}', '?', '+', '±', '|', '\'']
    illegalCharacters = illegalCharacters + guessedCharacters
    if(guessedCharacter[0] in illegalCharacters):
        return False
    else:
        return guessedCharacter[0]
