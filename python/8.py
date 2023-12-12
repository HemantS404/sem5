import sqlite3

con = sqlite3.connect("8.sqlite3")
cur = con.cursor()

# # creating table
# cur.execute("Create Table Student(id int, name varchar(50))")

# # inserting value
# cur.execute('Insert into student values (1,"Hemant")')
# con.commit()
# cur.execute('Insert into student values (2,"Shubham")')
# con.commit()

# # reading values
# res = cur.execute("Select * from student")
# for i in res:
#     uid, name = i
#     print(f"ID : {uid}, Name : {name}")

# # deleting a value
# cur.execute("delete from student where id=2")
# con.commit()

# # update values
# cur.execute("update student set name='Hemant Singh' where id=1")
# cur.execute("update student set name='Shubham Mehta' where id=2")
# con.commit()

# # alter table
# cur.execute("Alter table student rename to StudentDetails")
# con.commit()

# # drop table
# cur.execute("Drop table StudentDetails")
# con.commit()