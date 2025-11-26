from .consultas_dao import listar_paises
from .consultas_dao import Conneccion

class PaisManager:
    def __init__(self):
        self.paises = []
        self.cargar_paises()
    
    def cargar_paises(self):
        x = listar_paises()
        self.paises = [{'id': 0, 'Nombre': 'Seleccione Uno'}]
        for pais in x:
            self.paises.append({'id': pais[0], 'Nombre': pais[1]})
    
    def get_nombres(self):
        return [pais['Nombre'] for pais in self.paises]
    
    def get_id_por_indice(self, index):
        if 0 <= index < len(self.paises):
            return self.paises[index]['id']
        return None
    
    def get_indice_por_nombre(self, nombre):
        for i, pais in enumerate(self.paises):
            if pais['Nombre'] == nombre:
                return i
        return 0

#LO DEJO POR SI NECESITO CARGAR MAS DATOS
""" def guardar_pais(nombre):
    conn = Conneccion()
    sql = f"INSERT INTO Pais (Nombre) VALUES ('{nombre}');"
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
        print(f"País '{nombre}' agregado.")
    except Exception as e:
        print("Error al guardar país:", e) """
