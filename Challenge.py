# Python Ver : 3.8.3
#
# Author: Moise Ngoumape
#
# Purpose: Python Challenge
#
#
# Tested OS:  This code was written and tested to work with Windows 10.

import sqlite3


conn = sqlite3.Connection('roster.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_list(\
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_Name TEXT,\
                col_Species TEXT,\
                col_IQ TEXT\
    )")
    conn.commit()

conn = sqlite3.Connection('roster.db')
with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_list(col_Name,col_Species , col_IQ)VALUES(?,?,?)",\
                ('Jean-Baptiste Zorg', 'Human','122'))

cur.execute("INSERT INTO tbl_list(col_Name,col_Species , col_IQ)VALUES(?,?,?)",\
                ('Korben Dallas', 'Meat Popsicle','100'))
cur.execute("INSERT INTO tbl_list(col_Name,col_Species , col_IQ)VALUES(?,?,?)",\
                ('Ak''s''not','Human','122'))
#Update the Species of Korben Dallas to be Human
cur.execute("UPDATE col_Species SET Meat Popsicle = Human")
#Display the names IQs of everyone in the table who is classified as Human
print("Names IQs are:  ",(col_IQ))



if __name__ == "__main__":
    pass
