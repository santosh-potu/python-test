import mysql.connector


cnx = mysql.connector.connect(user='root',database='php_tutorial')
cursor = cnx.cursor()

cursor.execute("SELECT * From messages")
row = cursor.fetchone()
while row is not None:
    print(row)
    row = cursor.fetchone()

while row in cursor:
    print(row)
    
cursor.close()
cnx.close()