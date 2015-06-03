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
        characters = methods.character_count(randomString)
        while True:
            print(characters)
            i = input("Guess a character ")
            if not i:
                cur.close()
                conn.close()
                return

        Syntax = 'WHERE NOT word IN({})'.format(methods.character_array(ar))