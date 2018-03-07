#!/usr/bin/python3

import MySQLdb, json

db = MySQLdb.connect(host="45.77.REDACTED",    # your host, usually localhost
                     user="tor",         # your username
                     passwd="REDACTED",  # your password
                     db="torstats")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM transcriptions")


trans = []
# print all the first cell of all the rows
for row in cur.fetchall():
    trans.append({
        "transcriber": row[1],
        "content": row[2]
    })

with open("tr.txt", "w") as f:
    f.write("\n".join([json.dumps(t) for t in trans]))

db.close()
