import sqlite3 

database = sqlite3.connect("db.sqlite3")
cursor = database.cursor()

query = "select name from sqlite_schema where type = 'table' and name not like 'sqlite_%'"

query2 = "update employees_member set username = '' "

cursor.execute(query)
output = cursor.fetchall()
print(output)