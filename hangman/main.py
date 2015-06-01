
# Install PyMySQL --------- pip3 install PyMySQL
import pymysql
conn = pymysql.connect(db='python-hangman', user='python', passwd='python', host='localhost')

cur = conn.cursor()

cur.execute("SELECT word FROM dictionary ORDER BY RAND() LIMIT 1")

# print(cur.description)
random_string = cur.fetchone()[0]
print(random_string)

word_lenght = (len(random_string))

i = 0

for i in range(i,word_lenght):
    print("_ ", end=" ")


#TODO: get number of characters from string and insert as _ in console - DONE MBN
#TODO: After each guess, if correct, remove _ and replace with the guessed character at each respective character placement
#TODO: Maximum of 10 guesses (vi kan altid lave det om)
#TODO: Funsies, draw a hangman in console

# for row in cur:
#    print(row)




cur.close()
conn.close()