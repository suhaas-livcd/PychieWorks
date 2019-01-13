# -*- coding: utf-8 -*-
import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect('test.db')

    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')

    data = cur.fetchone()

    print("SQLite version: {}".format(data))
    
    cur = con.cursor()
    with con:

        cur = con.cursor()
        cur.execute("SELECT * FROM cars")
    
        rows = cur.fetchall()
    
        for row in rows:
            print(row)
#    cur.execute("CREATE TABLE cars(id INT, name TEXT, price INT)")
#    cur.execute("INSERT INTO cars VALUES(1,'Audi',52642)")
#    cur.execute("INSERT INTO cars VALUES(2,'Mercedes',57127)")
#    cur.execute("INSERT INTO cars VALUES(3,'Skoda',9000)")
#    cur.execute("INSERT INTO cars VALUES(4,'Volvo',29000)")
#    cur.execute("INSERT INTO cars VALUES(5,'Bentley',350000)")
#    cur.execute("INSERT INTO cars VALUES(6,'Citroen',21000)")
#    cur.execute("INSERT INTO cars VALUES(7,'Hummer',41400)")
#    cur.execute("INSERT INTO cars VALUES(8,'Volkswagen',21600)")
#    con.commit()
    cur = con.cursor()
    cur.execute("SELECT * FROM cars")

    rows = cur.fetchall()

    for row in rows:
        print(row)
#except lite.Error, e:
#    print("Error {}:".format(e.args[0]))
#    sys.exit(1)

finally:

    if con:
        con.close()
