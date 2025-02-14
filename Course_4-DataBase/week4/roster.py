import json
import sqlite3

connection = sqlite3.connect('rosterdb.sqlite')
cur = connection.cursor()

cur.execute('DROP TABLE IF EXISTS User')
cur.execute('DROP TABLE IF EXISTS Course')
cur.execute('DROP TABLE IF EXISTS Member')


cur.execute('''
            
    CREATE TABLE User(
        
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
        name TEXT UNIQUE      
    )
''')

cur.execute('''
            
    CREATE TABLE Course(
        
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
        title TEXT UNIQUE      
    )
''')

cur.execute('''
            
    CREATE TABLE Member(
        
        user_id INTEGER, 
        course_id INTEGER,
        role INTEGER,
        PRIMARY KEY(user_id, course_id)    
    )
''')

fh = open('roster_data.json', 'r', encoding="utf-8")
dados = json.load(fh)

for i in dados:
    if len(i) == 3:
        user_name = i[0]
        course_title = i[1]
        role = i[2]
    else:
        user_name = i[0]
        role = i[1]
    
    cur.execute('INSERT OR IGNORE INTO User(name) VALUES (?)', (user_name,))
    cur.execute('INSERT OR IGNORE INTO Course(title) VALUES (?)', (course_title,))
    
    cur.execute('SELECT id FROM User WHERE name = ?', (user_name,))
    name_aux = cur.fetchone()
    cur.execute('SELECT id FROM Course WHERE title = ?', (course_title,))
    course_title_aux = cur.fetchone()
    
    cur.execute('INSERT OR IGNORE INTO Member(user_id, course_id, role) VALUES (?, ?, ?)', (name_aux[0], course_title_aux[0], role))


connection.commit()
connection.close()