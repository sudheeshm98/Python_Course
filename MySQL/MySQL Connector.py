import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='root',password='sudhi@123')
# print(mydb)

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mydb_python")


# mycursor.execute("show databases")
# for x in mycursor:
#     print(x)


mycursor.execute("use mydb_python")
# mycursor.execute("CREATE TABLE Employee (Name VARCHAR(250),Dept VARCHAR(300),Salary INT(10))")


# mycursor.execute("show tables")
# for x in mycursor:
#     print(x)


# sql = "insert into Employee values ('jack','python',50000)"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount,"record inserted")


# sql = "insert into Employee (Name,Dept,Salary) values(%s,%s,%s)"
# val = [
#     ('rose','python',40000),
#     ('john','python',60000),
#     ('don','python',75000),
#     ('angel','python',80000)
# ]
# mycursor.executemany(sql,val)
# mydb.commit()
# print(mycursor.rowcount,"record inserted")


# mycursor.execute("select * from Employee")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# myresult = mycursor.fetchone()
# print(myresult)


# sql = "delete from Employee where name = 'don' "
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount,"records deleted")





