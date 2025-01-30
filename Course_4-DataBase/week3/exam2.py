import sqlite3

connection = sqlite3.connect('exam2db.sqlite')
cur = connection.cursor()

cur.execute('DROP TABLE IF EXISTS Track')
cur.execute('DROP TABLE IF EXISTS Album')
cur.execute('DROP TABLE IF EXISTS Genre')
cur.execute('DROP TABLE IF EXISTS Artist')

cur.execute('''
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);''')

cur.execute('''
CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
)''')

cur.execute('''
CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);''')

cur.execute('''
CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, 
    rating INTEGER, 
    count INTEGER
);''')

artist_id = 1
genre_id = 1
album_id = 1
teste = 1
fh = open('tracks.csv', encoding='utf-8')
for line in fh:
    
    pieces = line.split(",")

    music_name = pieces[0]
    artist_name = pieces[1]
    album_name = pieces[2]
    len = pieces[3]
    rating = pieces[4]
    count = pieces[5]
    genre_name = pieces[6].strip() 

    cur.execute('SELECT name FROM Artist WHERE name = ? ', (artist_name,))
    artist_aux = cur.fetchone()
   
    if artist_aux is None:
        cur.execute('''INSERT INTO Artist (id, name) VALUES (?, ?)''', (artist_id, artist_name))
        artist_id = artist_id+1 

    cur.execute('SELECT name FROM Genre WHERE name = ? ', (genre_name,))
    genre_aux = cur.fetchone()
   
    if genre_aux is None:
        cur.execute('''INSERT INTO Genre (id, name) VALUES (?, ?)''', (genre_id, genre_name))
        genre_id = genre_id+1 

    cur.execute('SELECT title FROM Album WHERE title = ? ', (album_name,))
    album_aux = cur.fetchone()
   
    if album_aux is None:
        
        cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist_name,))
        get_id = cur.fetchone()
        
        cur.execute('''INSERT INTO Album (id, artist_id, title) VALUES (?, ?, ?)''', (album_id, get_id[0], album_name))
        album_id = album_id+1 

    cur.execute('SELECT title FROM Track WHERE title = ? ', (music_name,))
    track_aux = cur.fetchone()
   
    if track_aux is None:
        
        cur.execute('SELECT id FROM Album WHERE title = ? ', (album_name,))
        get_id_album = cur.fetchone()

        cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre_name,))
        get_id_genre = cur.fetchone()

        cur.execute('''INSERT INTO Track (id, title, album_id, genre_id, len, rating, count) 
                    VALUES (?, ?, ?, ?, ?, ?, ?)''', (track_id, music_name, get_id_album[0], get_id_genre[0], len, rating, count))
        track_id = track_id+1 


connection.commit()
connection.close()