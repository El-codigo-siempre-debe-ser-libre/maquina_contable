
""" Llamo la aplicacion de contabilidad """


"===================================="

from contabiliza import Actividad

if __name__ == "__main__":
    
    ventana= Actividad()
    ventana.title("Mi maquina contable")
    ventana.geometry("600x300")
    #ventana.iconbitmap("c:\\mis_iconos\\finanzas.ico")
    ventana.resizable(0,0)

    ventana.mainloop()
    
"===================================="

