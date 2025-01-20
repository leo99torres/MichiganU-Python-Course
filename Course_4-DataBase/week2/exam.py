import sqlite3

connection = sqlite3.connect('emaildb.sqlite')
cur = connection.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')
top10=0
 
fh = open('mbox.txt', encoding='utf-8')
for line in fh:
    if line.startswith('From: '): 
        pieces = line.split()
        email = pieces[1]
        org = email.split('@')[1]
        cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
        row = cur.fetchone()
    
        if row is None:
            cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (org,)) 
        else:
            cur.execute('UPDATE Counts set count = count + 1 WHERE org = ?', (org,))
    
    

connection.commit()

sql_query = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for line in cur.execute(sql_query):
    print(line)
