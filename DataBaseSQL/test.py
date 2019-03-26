import  mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'imvivek71',
    database = 'testdb'
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
# for many queries

record =mycursor.fetchall()
print(record)


for tb in mycursor:
    print(tb)

    
