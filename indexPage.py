#!C:/Users/hjesi/AppData/Local/Programs/Python/Python312/python.exe
print("content-type:text/html \r\n\r\n")

# import pymysql
# connection = pymysql.connect(host="localhost", user="root", password="", database="")
# cur = connection.cursor()
# a = """ create database result"""
# cur.execute(a)
# connection.commit()
# connection.close()

import pymysql
connection = pymysql.connect(host="localhost", user="root", password="", database="result")
cur = connection.cursor()
a = """ create table marklist(sno int(10) auto_increment primary key, RegNo varchar(10), Name varchar(50), 
        RollNo varchar(10), DOB date, Language int(10), English int(10), Maths int(10), Physics int(10), 
        Chemistry int(10), CS int(10))"""
cur.execute(a)
connection.commit()
connection.close()
