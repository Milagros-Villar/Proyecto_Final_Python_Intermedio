from .coneciondb import Conneccion

 
# CREAR TABLAS
 

def crear_tabla():
    conn = Conneccion()

    sql= '''
        CREATE TABLE IF NOT EXISTS Genero(
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Nombre VARCHAR(50)
        );

        CREATE TABLE IF NOT EXISTS Peliculas(
            ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            Nombre VARCHAR(150),
            Duracion VARCHAR(4),
            Genero INTEGER,
            Pais INTEGER,
            Anio VARCHAR(4),
            FOREIGN KEY (Genero) REFERENCES Genero(ID),
            FOREIGN KEY (Pais) REFERENCES Pais(ID)
        );
    '''
    try:
        conn.cursor.executescript(sql)
        conn.cerrar_con()
    except:
        pass


def crear_tabla_pais():
    conn = Conneccion()
    sql = '''
        CREATE TABLE IF NOT EXISTS Pais(
            ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            Nombre VARCHAR(100)
        );
    '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print("Error creando tabla Pais:", e)


 
# CLASE PELICULAS
 
class Peliculas():

    def __init__(self,nombre,duracion,genero,pais,anio):
       self.nombre = nombre
       self.duracion = duracion
       self.genero = genero
       self.pais = pais
       self.anio = anio

    def __str__(self):
        return f'Pelicula[{self.nombre},{self.duracion},{self.genero},{self.pais},{self.anio}]'


 
# CRUD
 

def guardar_peli(pelicula):
    conn = Conneccion()

    sql= f'''
        INSERT INTO Peliculas(Nombre,Duracion,Genero,Pais,Anio)
        VALUES('{pelicula.nombre}','{pelicula.duracion}',{pelicula.genero},{pelicula.pais},'{pelicula.anio}');
    '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print("Error guardando:", e)

def listar_peli():
    conn = Conneccion()

    sql= '''
        SELECT p.ID, p.Nombre, p.Duracion, g.Nombre, pa.Nombre, p.Anio
        FROM Peliculas p
        INNER JOIN Genero g ON p.Genero = g.ID
        LEFT JOIN Pais pa ON p.Pais = pa.ID;
    '''

    try:
        conn.cursor.execute(sql)
        datos = conn.cursor.fetchall()
        conn.cerrar_con()
        return datos
    except Exception as e:
        print("Error listando:", e)
        return []


def listar_generos():
    conn = Conneccion()

    sql = 'SELECT id, nombre FROM Genero ORDER BY nombre;'

    try:
        conn.cursor.execute(sql)
        resultados = conn.cursor.fetchall()
        conn.cerrar_con()
        return resultados
    except:
        return []

# ACA CREE LA DE PELICULAS
def listar_paises():
    conn = Conneccion()
    sql = 'SELECT id, nombre FROM Pais ORDER BY nombre;'

    try:
        conn.cursor.execute(sql)
        resultados = conn.cursor.fetchall()
        conn.cerrar_con()
        return resultados
    except:
        return []


def editar_peli(pelicula, id):
    conn = Conneccion()

    sql= f'''
        UPDATE Peliculas
        SET Nombre = '{pelicula.nombre}', 
            Duracion = '{pelicula.duracion}', 
            Genero = {pelicula.genero},
            Pais = {pelicula.pais},
            Anio = '{pelicula.anio}'
        WHERE ID = {id};
    '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print("Error editando:", e)

def borrar_peli(id):
    conn = Conneccion()

    sql= f'''
        DELETE FROM Peliculas WHERE ID = {id};
    '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass
