
# Install PyMySQL --------- pip3 install PyMySQL
import pymysql
conn = pymysql.connect(db='python-hangman', user='python', passwd='python', host='localhost')

cur = conn.cursor()

cur.execute("SELECT word FROM dictionary ORDER BY RAND() LIMIT 1")

# print(cur.description)

print(cur.fetchone()[0])
# for row in cur:
#    print(row)

cur.close()
conn.close()