
# Install PyMySQL --------- pip3 install PyMySQL
import pymysql

conn = pymysql.connect(db='python-hangman', user='python', passwd='python', host='localhost')
cur = conn.cursor()
cur.execute("SELECT word FROM dictionary ORDER BY RAND() LIMIT 1")

lives = 10
guessCount = 0

random_string = cur.fetchone()[0]

#gets lenght of word
word_lenght = (len(random_string))

#print lenght as "_" characters on same line
i = 0
for i in range(i,word_lenght):
    print("_ ", end=" ")

if guessCount == lives:
    print("you failed...")
else:
    print("lets play..")


#TODO: After each guess, if correct, remove _ and replace with the guessed character at each respective character placement
#TODO: Maximum of 10 guesses (vi kan altid lave det om)
#TODO: Funsies, draw a hangman in console

cur.close()
conn.close()