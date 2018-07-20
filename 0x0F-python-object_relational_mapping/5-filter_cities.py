#!/usr/bin/python3
'''Script that lists all states from the database hbtn_0e_0_usa'''

if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name \
                FROM states \
                JOIN cities ON states.id = cities.state_id \
                WHERE states.name = %s \
                ORDER BY cities.id ASC", (argv[4],))
    rows = cur.fetchall()
    l = []
    for row in rows:
        l.append(row[1])
    print(', '.join(l))
    cur.close()
    db.close()
