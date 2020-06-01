import sqlite3

conn = sqlite3.Connection('name.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_list(\
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT,\
            col_lname TEXT,\
            col_document TEXT\
               ) ")
    conn.commit()
conn.close()

conn = sqlite3.connect('name.db')
fileList = ['information.docx','Hello.txt','myImage.png','myMovie.mpg','World.txt','data.pdf','myPhoto.jpg']
 for name in fileList:
     print(name)
     cur.execute("INSERT INTO tbl_list(fileList)VALUES()",)

     Page number(Step 162)
