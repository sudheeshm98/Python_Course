import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='root',password='sudhi@123')

mycursor = mydb.cursor()

# mycursor.execute("use mydb_python")
# mycursor.execute("CREATE TABLE Student (Name VARCHAR(250),Course VARCHAR(300),Score INT(10))")

mycursor.execute("use mydb_python")

# sql = "insert into Student (Name,Course,Score) values(%s,%s,%s)"
# val = [
#     ('rose','python',80),
#     ('john','python',76),
#     ('don','python',99),
#     ('angel','python',85),
#     ('jack','python',90)
# ]
# mycursor.executemany(sql,val)
# mydb.commit()
# print(mycursor.rowcount,"record inserted")