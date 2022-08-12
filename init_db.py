import sqlite3
#import sys
#import os


def criarDB(nbanco):
    #database = os.path.dirname(sys.executable)
    #connection = sqlite3.connect(database + '/database.db')
    connection = sqlite3.connect(nbanco)

    #with open('schema.sql') as f:
    #    connection.executescript(f.read())

    connection.executescript(' DROP TABLE IF EXISTS posts; '+
                            ' CREATE TABLE posts ( ' +
                            '    id INTEGER PRIMARY KEY AUTOINCREMENT, '+
                            '    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, '+
                            '    title TEXT NOT NULL, '+
                            '    content TEXT NOT NULL '+
                            ' ); ')

    #cur = connection.cursor()

    #cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
    #            ('First Post', 'Content for the first post')
    #            )

    #cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
    #            ('Second Post', 'Content for the second post')
    #            )

    connection.commit()
    connection.close()