import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Mysql@123',
    database='furniture',
)
mycursor = mydb.cursor()
mycursor.execute("use furniture")
mycursor.execute("""create table cupboard(
    id int(15) not null,
    name varchar(75) not null,
    price float not null,
    count int not null,
    primary key(id)
)""")
sql = """insert into cupboard(id, name, price, count) values (%s, %s, %s, %s)"""
val = [
    (2, 'cb2', 15000, 5),
    (3, 'cb3', 7000, 15),
    (4, 'cb4', 20000, 3),
    (5, 'cb5', 40000, 5)
]
mycursor.executemany(sql, val)
mydb.commit()
mycursor.execute('select * from cupboard')
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
