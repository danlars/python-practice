
def character_guess(word, guessedCharacters):#Create underscore characters for each existing letter in word
    characters = ""
    for x in str(word).lower():
        if x in guessedCharacters:
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

