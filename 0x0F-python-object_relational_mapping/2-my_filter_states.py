#!/usr/bin/python3
"""Script that displays values in states table of hbtn_0e_0_usa
   where name matches the argument
"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    cur.close()
    db.close()
