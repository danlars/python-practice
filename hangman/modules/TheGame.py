from hangman.modules import methods
import pymysql

conn = pymysql.connect(db='python-hangman', user='python', passwd='python', host='localhost')
cur = conn.cursor()

def hangmanTheGame(name):
    Syntax = ""
    ar = []

    while True:
        if not cur.execute("SELECT word FROM dictionary {} ORDER BY RAND() LIMIT 1".format(Syntax)):
            print("Congratulations! to " + name + " You have beaten the game!")
            break

        randomString = cur.fetchone()[0]
        ar.append(randomString)
        characters = None

        for i in randomString:
            characters += "_"

        #number of tries
        tries_left = 10

        while tries_left > 0:


            print("You have %d live(s) left" % tries_left)
            print(characters)
            i = input("Guess a character ")
            characters = methods.character_guess(randomString, i)
            # if user guess is not in word decrement tries_left by one
            if i not in randomString:
                tries_left=-1
            else:
                index = (randomString.rfind(i))
                print(index)

            if not i: #If no input is received, stop the game
                cur.close()
                conn.close()
                return

        Syntax = 'WHERE NOT word IN({})'.format(methods.MySQLWords(ar))


