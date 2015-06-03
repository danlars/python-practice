
def character_count(word):
    characters = ""
    for x in word:
        characters += "-"
    return characters

def character_array(ar):
    count = 0
    stringArrays = ""

    for row in ar:
        if count == 0:
            count = 1
            stringArrays += '\'{}\''.format(row)
        else:
            stringArrays += ',\'{}\''.format(row)

    return stringArrays