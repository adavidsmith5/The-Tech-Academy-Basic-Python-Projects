import sqlite3

conn = sqlite3.connect('dBPractice.db')

fileList = ('information.docx','Hello.txt','myImage.png','myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
txtFiles = []
for file in fileList:
    if file.endswith('.txt'):
        txtFiles.append(file)

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_textFiles(\
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    col_fileName TEXT \
    )")
    conn.commit()

    for file in txtFiles:
        cur.execute("INSERT INTO tbl_textFiles(col_fileName) VALUES (?)", \
                ('{}'.format(file),))
        conn.commit()
    
conn.close()
for file in txtFiles:
    print(file)
