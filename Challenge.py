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
    cur.execute("INSERT INTO tbl_list(col_Name)VALUES(?,?,?)",\
                ('Jean-Baptiste Zorg', 'Korben Dallas','Aknot'))





if __name__ == "__main__":
    pass
