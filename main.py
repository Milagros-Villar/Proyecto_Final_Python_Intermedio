import tkinter as tk
from vista.vista import Frame
from include.menu import barrita_menu
from modelo.consultas_dao import crear_tabla_pais
# from modelo.paises_dao import guardar_pais   # IMPORTANTE PARA CARGAR NOMBRES

def main():

    # Crear tabla Pais si no existe
    crear_tabla_pais()
    ventana = tk.Tk()
    ventana.title('Listado Peliculas')
    ventana.iconbitmap('img/videocamara.ico')
    ventana.resizable(0,0)

    barrita_menu(ventana)
    app = Frame(root=ventana)

    ventana.mainloop()


if __name__ == '__main__':
    main()
