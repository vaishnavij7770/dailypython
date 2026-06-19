import sqlite3 as sq

con=sq.connect("core.db")
cur=con.cursor()
# cur.execute("create table if not exists joinee(id int,name varchar(10),sal int)")
# cur.execute("insert into joinee(111,'python',838932)")
# cur.execute("insert into joinee values(?,?,?)",(114,'testing',1234))

# a=input("enter id")
# b=input("enter name")
# c=input("enter sal")

# cur.execute("insert into joinee values(?,?,?)", (a, b, c))

# list1=[(115,"xyz",456),(114,"efhj",344),(222,"ejed",83348)]
# cur.executemany("insert into joinee values(?,?,?)",list1)

# data=cur.execute("select * from joinee")
# print(data)

cur.execute("select * from joinee")
data=cur.fetchall()

cur.execute("select * from joinee where id=?",[111])
data=cur.fetchone()

print(data)


# for i in data:
#     #print(i)
#     print(i[0],i[1],i[2])
con.commit()
con.close()