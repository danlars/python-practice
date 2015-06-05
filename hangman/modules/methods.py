
def character_guess(word, characterGuessed, guessedCharacter = ""):#Create underscore characters for each existing letter in word
    characters = ""
    for x in word:
        if guessedCharacter == x or "_" not in x :
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

