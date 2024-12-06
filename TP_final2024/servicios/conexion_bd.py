import sqlite3

##conexion a la database

conexion = sqlite3.connect('anime.db')
cursor = conexion.cursor()

cursor.execute(
     
     '''
     CREATE TABLE IF NOT EXISTS anime(
     id INTEGER PRIMARY KEY AUTOINCREMENT,  
     titulo TEXT CHECK(length(titulo) <= 100),  
     resumen TEXT CHECK(length(resumen) <= 300),  
     director TEXT CHECK(length(director) <= 50), 
     categoria TEXT,
     año INTEGER,
     episodios INTEGER,
     rating REAL,
     precio REAL,
     stock INTEGER
);
     
     '''
)
conexion.commit()