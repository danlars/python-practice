
def character_count(word):#Create underscore characters for each existing letter in word
    characters = ""
    for x in word:
        characters += "-"
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