import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='root',charset='utf8')
cur=con.cursor()

cur.execute("create database if not exists practical")
cur.execute("use practical")

cur.execute("create table if not exists student (roll int primary key, name char(20),stipend int, stream char(10), avgmark numeric(5,2), grade char, class int)")
print("Table created")

cur.execute("insert ignore into student values(101,'Karan',400,'Medical', 78.5,'B',12)")
cur.execute("insert ignore into student values(102,'Divakar',450,'Commerce', 89.5,'A',11)")
cur.execute("insert ignore into student values(103,'Divya',300,'Commerce', 68.6,'C',12)")
cur.execute("insert ignore into student values(104,'Arun',350,'Medical', 85.5,'D',12)")
cur.execute("insert ignore into student values(105,'Sophy',600,'Biology', 90.3,'A',11)")

con.commit()
print("Records inserted")

cur.execute("select sum(stipend) from student where grade='a'" )
data=cur.fetchall()
print(4)
for x in data:
    print(x)

