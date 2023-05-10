import sqlite3

conn = sqlite3.connect('aula_database') 
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS usuarios(
            usuario_id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_name VARCHAR(25),
            usuario_senha VARCHAR(25)
          )
          ''')

conn.commit()