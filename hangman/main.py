
# Install PyMySQL --------- pip3 install PyMySQL
import pymysql
conn = pymysql.connect(db='python-hangman', user='python', passwd='python', host='localhost')

cur = conn.cursor()

cur.execute("SELECT * FROM dictionary")

print(cur.description)

for row in cur:
   print(row)

cur.close()
conn.close()
