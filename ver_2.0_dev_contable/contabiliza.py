
""" Desarrollo la aplicacion de contabilidad personal """


"==================================="

from genericpath import exists
import tkinter as tk
import sqlite3
import os

"==================================="

class Actividad(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.primera_variable= 0
        self.gusto_por_profesion= ""

        self.se_ha_completado_el_ahorro= False
        
        "........................"
        
        self.base_dato= None
        self.a_cambiar= None
        
        self.ya_a_reset_base_d= False
        
        "........................"
        
        self.ya_a_gastos_m= False
        self.a_cambiar_gasto= None

        "..............................................."

        os.makedirs("c:\\finanza_personal", exist_ok= True)

        if exists("c:\\finanza_personal\\info_fp.db"):
            pass
        else:
            print("hola creo")
            crea= open("c:\\finanza_personal\\info_fp.db", "w")
            crea.write("")
            crea.close()

        self.list_elements= [("deuda_inf", 0), ("colchon", 0), ("activos", 0), ("salario_q", 0)]

        "..............................................."
        
        self.marco= tk.LabelFrame(self)
        self.marco.pack(expand= True, fill= tk.BOTH)
        
        "..............................................."
                
        self.world_0= tk.LabelFrame(self.marco, bg= "orange")
        self.world_0.pack(expand= True, fill= tk.BOTH)
        self.world_1= tk.LabelFrame(self.marco, bd= 0)
        self.world_2= tk.LabelFrame(self.marco, bd= 0)
        self.world_3= tk.LabelFrame(self.marco, bd= 0)
        self.world_4= tk.LabelFrame(self.marco, bd= 0)

        self.resultados= tk.LabelFrame(self.marco, bd= 0)
        
        self.reset_base_d= tk.LabelFrame(self.marco, bd= 0)
        self.gastos= tk.LabelFrame(self.marco, bd= 0)
        self.edicion_gastos= tk.LabelFrame(self.marco, bd= 0)
        
        "..............................................."

        self.presentate()
    
    def saca_datos_db(self):
        
        self.valor_1= 0
        self.valor_2= 0
        self.valor_3= 0
        self.valor_4= 0
                
        if True: # Activa la Base de Dato

            info_fp= sqlite3.connect("c:\\finanza_personal\\info_fp.db")
            puerta= info_fp.cursor()
            
            def crear():
        
                puerta.execute("CREATE TABLE cuentas (nombre VARCHAR, valor INTEGER)")
                
                puerta.executemany("INSERT INTO cuentas VALUES (?, ?)", self.list_elements)
                info_fp.commit()
            
                puerta.execute("SELECT * FROM cuentas")
                self.base_dato= puerta.fetchall()
                info_fp.commit()
                
                info_fp.close()

            try:
                puerta.execute('SELECT * FROM cuentas')
                self.base_dato= puerta.fetchall()
                info_fp.commit()
                info_fp.close()

            except sqlite3.OperationalError:
                crear()
            
        if True: # Relleno las variables
            
            for e, i in enumerate(self.base_dato):
                
                if e == 0:
                    self.valor_1= i
                if e == 1:
                    self.valor_2= i
                if e == 2:
                    self.valor_3= i
                if e == 3:
                    self.valor_4= i
    
    def presentate(self):
        
        self.nuevavent= tk.Toplevel(self.marco)
        self.nuevavent.focus()
        self.nuevavent.title("presentacion")
        self.nuevavent.geometry("600x300")
        #self.nuevavent.iconbitmap("c:\\mis_iconos\\finanzas.ico")
        
        self.saca_datos_db()

        self.venta_1= tk.LabelFrame(self.nuevavent, bd= 0)
        self.venta_1.pack()
        self.venta_2= tk.LabelFrame(self.nuevavent, bd= 0)
        self.venta_rb= tk.LabelFrame(self.nuevavent, bd= 0)
        
        self.mensg= tk.LabelFrame(self.venta_1, bd= 0)
        self.mensg.pack()
        self.entrada= tk.Label(self.mensg, text= "¿ESTAMOS ASI CON LAS CUENTAS?")
        self.entrada.pack()
        
        self.separeit_0= tk.Label(self.venta_1, text= "").pack()
        
        self.question= tk.LabelFrame(self.venta_1)
        self.question.pack()
        self.entrada_boton_1= tk.Button(self.question, text= "Si", padx= 25, pady= 20, bd= 4, command= self.cuenta_0)
        self.entrada_boton_2= tk.Button(self.question, text= "No", padx= 25, pady= 20, bd= 4, command= self.reset_base_dato)
        self.espacio= tk.Label(self.question, text= "      ")
        self.espacio.grid(row= 0, column= 1)
        self.entrada_boton_1.grid(row= 0, column= 0)
        self.entrada_boton_2.grid(row= 0, column= 2)

        self.separeit_01= tk.Label(self.venta_1, text= "").pack()

        self.asiesta= tk.LabelFrame(self.venta_1, bd= 0)
        self.asiesta.pack()
        self.dato_1= tk.Label(self.asiesta, text= "En deuda informal debes:", padx= 10, pady= 10)
        self.dato_1.grid(row= 0, column= 0)
        self.dato_2= tk.Label(self.asiesta, text= "En colchon inadvertido tienes:", padx= 10, pady= 10)
        self.dato_2.grid(row= 1, column= 0)
        self.dato_3= tk.Label(self.asiesta, text= "En activos tienes invertido:", padx= 10, pady= 10)
        self.dato_3.grid(row= 2, column= 0)
        self.dato_4= tk.Label(self.asiesta, text= "Tu salario promedio quincenal es:", padx= 10, pady= 10)
        self.dato_4.grid(row= 3, column= 0)
        #
        self.ans_1= tk.Label(self.asiesta, text= self.valor_1[1], padx= 10, pady= 10)
        self.ans_1.grid(row= 0, column= 1)
        self.ans_2= tk.Label(self.asiesta, text= self.valor_2[1], padx= 10, pady= 10)
        self.ans_2.grid(row= 1, column= 1)
        self.ans_3= tk.Label(self.asiesta, text= self.valor_3[1], padx= 10, pady= 10)
        self.ans_3.grid(row= 2, column= 1)
        self.ans_4= tk.Label(self.asiesta, text= self.valor_4[1], padx= 10, pady= 10)
        self.ans_4.grid(row= 3, column= 1)
        
        self.nuevavent.withdraw()
        self.nuevavent.iconify()

    def back(self):
        
        self.venta_rb.forget()
        self.venta_1.pack()
        
        self.saca_datos_db()
        
        self.ans_1["text"]= self.valor_1[1]
        self.ans_2["text"]= self.valor_2[1]
        self.ans_3["text"]= self.valor_3[1]
        self.ans_4["text"]= self.valor_4[1]

    def which(self, cual):
        
        self.par_dato= None
        
        if cual == 1:
            self.a_cambiar= 1
            self.par_dato= self.valor_1
        elif cual == 2:
            self.a_cambiar= 2
            self.par_dato= self.valor_2
        elif cual == 3:
            self.a_cambiar= 3
            self.par_dato= self.valor_3
        elif cual == 4:
            self.a_cambiar= 4
            self.par_dato= self.valor_4

        self.mencion["text"]= "La eleccion es: " + str(cual)

        self.saca_datos_db()
        self.tal_valor_esta["text"]= "Su valor es de: " + str(self.par_dato[1])

    def actualiza(self):
        
        nuevo_dato= self.rescribo.get()
        
        nombre= self.par_dato[0]
        name= str(nombre)
                
        new_busq= sqlite3.connect("c:\\finanza_personal\\info_fp.db")
        rebobina= new_busq.cursor()
        
        rebobina.execute("UPDATE cuentas SET valor= {0} WHERE nombre= '{1}'".format(nuevo_dato, name))
        
        new_busq.commit()
        new_busq.close()

        self.tal_valor_esta["text"]= "Su valor es de: " + str(nuevo_dato)
        self.rescribo.delete(0, tk.END)

    def reset_base_dato(self):
        
        if self.ya_a_reset_base_d == False:
            
            self.venta_1.forget()
            self.venta_rb.pack()
            
            self.separa_rb= tk.Label(self.venta_rb, text= "").pack()

            self.escoge= tk.LabelFrame(self.venta_rb)
            self.escoge.pack()
                                
            self.bo_1= tk.Button(self.escoge, text= "deuda_inf", command= lambda:self.which(1))
            self.bo_1.grid(row= 0, column= 0)
            self.bo_2= tk.Button(self.escoge, text= "colchon", command= lambda:self.which(2))
            self.bo_2.grid(row= 0, column= 1)
            self.bo_3= tk.Button(self.escoge, text= "activos", command= lambda:self.which(3))
            self.bo_3.grid(row= 0, column= 2)
            self.bo_4= tk.Button(self.escoge, text= "salario_q", command= lambda:self.which(4))
            self.bo_4.grid(row= 0, column= 3)

            self.mencion= tk.Label(self.venta_rb, text= "La eleccion es:")
            self.mencion.pack()
            
            self.tal_valor_esta= tk.Label(self.venta_rb, text= "Su valor es de:")
            self.tal_valor_esta.pack()

            "......................................"

            self.separa_rb= tk.Label(self.venta_rb, text= "").pack()

            self.ingresando= tk.LabelFrame(self.venta_rb, bd= 0)
            self.ingresando.pack()

            self.ingresa= tk.Label(self.ingresando, text= "Ingrese el nuevo valor: ")
            self.ingresa.grid(row= 0, column= 0)

            self.rescribo= tk.Entry(self.ingresando)
            self.rescribo.grid(row= 0, column= 1)
            
            "......................................"

            self.updata= tk.Button(self.venta_rb, text= "actualiza", command= self.actualiza)
            self.updata.pack()

            "..............................................."

            self.separa_rb= tk.Label(self.venta_rb, text= "").pack()

            self.backing= tk.Button(self.venta_rb, text= "BACK", command= self.back)
            self.backing.pack()

            self.ya_a_reset_base_d= True

        else:
            self.venta_1.forget()
            self.venta_rb.pack()

    def cuenta_0(self):
                
        self.venta_1.forget()
        self.venta_2.pack()
        
        self.separeit_1= tk.Label(self.venta_2, text= "").pack()

        self.mira_0= tk.Label(self.venta_2, text= "  ¿Cual es tu Motivacion, la que te lleva a la actividad Laboral? : ")
        self.mira_0.pack()
        self.text_0= tk.Entry(self.venta_2, width= 35)
        self.text_0.pack()
                
        self.separeit_2= tk.Label(self.venta_2, text= "").pack()
        
        self.mira_1= tk.Label(self.venta_2, text= "Dime... ¿Cual es la profesion que sabes y a la vez, en la que te gusta trabajar? : ")
        self.mira_1.pack()
        self.text_1= tk.Entry(self.venta_2, width= 35)
        self.text_1.pack()
        
        self.separeit_3= tk.Label(self.venta_2, text= " \n ").pack()
        
        self.conti_dos= tk.LabelFrame(self.venta_2)
        self.conti_dos.pack()
        
        self.sigue= tk.Button(self.conti_dos, text= "Siguiente ==>", padx= 40, pady= 30, command= self.espera)
        self.sigue.pack()


    def espera(self):
        
        self.gusto_por_profesion= self.text_1.get()
        self.nuevavent.withdraw()

        self.separa_0= tk.Label(self.world_0, pady= 10, bg= "orange", text= "").pack()

        self.pric_msg= tk.Label(self.world_0, text= "TODAS LAS CIFRAS SIGUIENTES LAS HAS DE INGRESAR EN... MILES DE  $")
        self.pric_msg.pack()

        self.separa_1= tk.Label(self.world_0, pady= 10, bg= "orange", text= "").pack()

        self.sgte= tk.Button(self.world_0, text= "OK", padx= 40, pady= 30, command= self.cuenta_1)
        self.sgte.pack()
    
    
    def operacion_1(self, complejidad):
        
        valor_neto= self.text_1.get()
        
        de_basico= self.text_2.get()
        de_deuda_informal= self.text_3.get()
        
        le_quito= int(de_basico) + int(de_deuda_informal)
        
        self.primera_variable= int(valor_neto) - le_quito
        
        if complejidad == 0:
            self.cuenta_2()
        elif complejidad == 1:
            self.gastos_m()
            
    def cuenta_1(self):
        
        self.world_0.forget()
        self.world_1.pack()
                
        self.separeit_4= tk.Label(self.world_1, text= "").pack()
        
        el_doble=  int(self.valor_4[1]) * 2

        self.pregunta_0= tk.Label(self.world_1, text= "Tu sueldo es de {} mil \nPero, menos tu deuda Formal (del banco), te quedan ¿cuanto?".format(el_doble))
        self.pregunta_0.pack()
        self.text_1= tk.Entry(self.world_1)
        self.text_1.pack()
        
        self.pregunta_1= tk.Label(self.world_1, text= "Con... la Donacion, Alimentacion y Consumo en la Labor, Le quitas ¿cuanto?")
        self.pregunta_1.pack()
        self.text_2= tk.Entry(self.world_1)
        self.text_2.pack()
        
        self.pregunta_2= tk.Label(self.world_1, text= "Dime... ¿Cuanto has apartado de la deuda Informal?")
        self.pregunta_2.pack()
        self.text_3= tk.Entry(self.world_1)
        self.text_3.pack()

        self.separeit_5= tk.Label(self.world_1, text= "").pack()

        self.maqueta_0= tk.LabelFrame(self.world_1)
        self.maqueta_0.pack()
        self.indagacion= tk.Label(self.maqueta_0, text= "Quieres ingresar a la seccion de gastos mayores y menores", padx= 10, pady= 5, bd= 4)
        self.indagacion.pack()
        
        self.maqueta_1= tk.LabelFrame(self.world_1)
        self.maqueta_1.pack()
        self.boton_0= tk.Button(self.maqueta_1, text= "Si", padx= 74, pady= 10, command= lambda:self.operacion_1(1))
        self.boton_0.grid(row= 0, column= 0)
        self.boton_1= tk.Button(self.maqueta_1, text= "No", padx= 74, pady= 10, command= lambda:self.operacion_1(0))
        self.boton_1.grid(row= 0, column= 1)
        
    def operacion_gastos(self):
        
        set_1= self.gasta_1[1] + self.gasta_2[1]
        set_2= self.gasta_3[1] + self.gasta_4[1] + self.gasta_5[1]
        
        a_quitar= set_1 + set_2
        
        self.primera_variable -= a_quitar
        
    def extrae_db_gasto(self):
        
        def creacion():
            
            list_gast= [("my_aporte_o", 0), ("my_aporte_f", 0),
                        ("mm_salud_p", 0), ("un_producto", 0), ("un_valor", 0)]
            
            fucelaje= sqlite3.connect("c:\\finanza_personal\\info_fp.db")
            puerta_22= fucelaje.cursor()
            
            puerta_22.execute("CREATE TABLE gastos (tipo VARCHAR, valor INTEGER)")
            puerta_22.executemany("INSERT INTO gastos VALUES (?, ?)", list_gast)
            fucelaje.commit()
            
            fucelaje.close()
        
        aplicando_f= sqlite3.connect("c:\\finanza_personal\\info_fp.db")
        puerta_24= aplicando_f.cursor()
        
        try:
            puerta_24.execute("SELECT * FROM gastos")
            
        except sqlite3.OperationalError:
            creacion()
            puerta_24.execute("SELECT * FROM gastos")
        
        valores_gast= puerta_24.fetchall()
        aplicando_f.commit()
        
        aplicando_f.close()
        
        self.gasta_1= 0
        self.gasta_2= 0
        self.gasta_3= 0
        self.gasta_4= 0
        self.gasta_5= 0
        
        for m, t in enumerate(valores_gast): # coloco cada elemento en un "gasta_"
            
            if m == 0:
                self.gasta_1= t
            if m == 1:
                self.gasta_2= t
            if m == 2:
                self.gasta_3= t
            if m == 3:
                self.gasta_4= t
            if m == 4:
                self.gasta_5= t
                
    def retorna_a_gasto(self):
        
        self.edicion_gastos.forget()
        self.gastos.pack(fill= tk.BOTH, expand= True)
        
        self.extrae_db_gasto()
        
        self.gast_11["text"]= self.gasta_1[1]
        self.gast_12["text"]= self.gasta_2[1]
        y_la_suma_1= self.gasta_1[1] + self.gasta_2[1]
        self.gast_13["text"]= y_la_suma_1
        
        self.gast_21["text"]= self.gasta_3[1]
        self.gast_22["text"]= self.gasta_4[1]
        self.gast_23["text"]= self.gasta_5[1]
        y_la_suma_2= self.gasta_3[1] + self.gasta_4[1] + self.gasta_5[1]
        self.gast_24["text"]= y_la_suma_2
        
    def dime_cuanto_gasto(self, dime):
        
        self.dato_select= None
        
        if dime == 1:
            self.a_cambiar_gasto= 1
            self.dato_select= self.gasta_1
        elif dime == 2:
            self.a_cambiar_gasto= 2
            self.dato_select= self.gasta_2
        elif dime == 3:
            self.a_cambiar_gasto= 3
            self.dato_select= self.gasta_3
        elif dime == 4:
            self.a_cambiar_gasto= 4
            self.dato_select= self.gasta_4
        elif dime == 5:
            self.a_cambiar_gasto= 5
            self.dato_select= self.gasta_5

        self.menciona["text"]= "La eleccion es: " + str(dime)

        self.extrae_db_gasto()
        self.tal_valor_es["text"]= "Su valor es de: " + str(self.dato_select[1])

    def actualiza_g(self):
        
        nuevo_dato= self.rescriba.get()
        
        nombre= self.dato_select[0]
        name= str(nombre)
        
        actual_gast= sqlite3.connect("c:\\finanza_personal\\info_fp.db")
        fucela= actual_gast.cursor()
        
        fucela.execute("UPDATE gastos SET valor= {0} WHERE tipo= '{1}'".format(nuevo_dato, name))
        actual_gast.commit()
        
        actual_gast.close()

        self.tal_valor_es["text"]= "Su valor es de: " + str(nuevo_dato)
        self.rescriba.delete(0, tk.END)

    def edit_gastos(self):
        
        if self.prim_edicion == False:
            
            self.gastos.forget()
            self.edicion_gastos.pack()

            "............................................."
            
            self.separa_gt= tk.Label(self.edicion_gastos, text= "").pack()

            self.escoge= tk.LabelFrame(self.edicion_gastos)
            self.escoge.pack()
                                
            self.bo_1= tk.Button(self.escoge, text= "my_aporte_O", command= lambda:self.dime_cuanto_gasto(1))
            self.bo_1.grid(row= 0, column= 0)
            self.bo_2= tk.Button(self.escoge, text= "my_aporte_f", command= lambda:self.dime_cuanto_gasto(2))
            self.bo_2.grid(row= 0, column= 1)
            self.bo_3= tk.Button(self.escoge, text= "mm_salud_p", command= lambda:self.dime_cuanto_gasto(3))
            self.bo_3.grid(row= 0, column= 2)
            self.bo_4= tk.Button(self.escoge, text= "un_producto", command= lambda:self.dime_cuanto_gasto(4))
            self.bo_4.grid(row= 0, column= 3)
            self.bo_5= tk.Button(self.escoge, text= "un_valor", command= lambda:self.dime_cuanto_gasto(5))
            self.bo_5.grid(row= 0, column= 4)

            self.menciona= tk.Label(self.edicion_gastos, text= "La eleccion es:")
            self.menciona.pack()
            
            self.tal_valor_es= tk.Label(self.edicion_gastos, text= "Su valor es de:")
            self.tal_valor_es.pack()

            "......................."

            self.separa_gt= tk.Label(self.edicion_gastos, text= "").pack()

            self.ingresan= tk.LabelFrame(self.edicion_gastos, bd= 0)
            self.ingresan.pack()

            self.ingress= tk.Label(self.ingresan, text= "Ingrese el nuevo valor: ")
            self.ingress.grid(row= 0, column= 0)

            self.rescriba= tk.Entry(self.ingresan)
            self.rescriba.grid(row= 0, column= 1)
            
            "......................."

            self.updat= tk.Button(self.edicion_gastos, text= "actualiza", command= self.actualiza_g)
            self.updat.pack()

            "............................................."

            self.separa_gt= tk.Label(self.edicion_gastos, text= "").pack()

            self.retorna= tk.Button(self.edicion_gastos, text= "Atras", command= self.retorna_a_gasto)
            self.retorna.pack()
            
            self.prim_edicion= True
            
        else:
            self.gastos.forget()
            self.edicion_gastos.pack()
    
    def gastos_m(self):
        
        self.extrae_db_gasto()
        
        self.world_1.forget()
        self.gastos.pack(fill= tk.BOTH, expand= True)
        
        self.de_dos= tk.LabelFrame(self.gastos)
        self.de_dos.pack(fill= tk.BOTH, expand= True, side= "top")
        
        self.uno= tk.LabelFrame(self.de_dos, bg= "yellow")
        self.uno.pack(fill= tk.BOTH, expand= True, side= "left")
        
        self.dos= tk.LabelFrame(self.de_dos, bg= "red")
        self.dos.pack(fill= tk.BOTH, expand= True, side= "right")

        "............................................."

        self.espac= tk.Label(self.uno, text= "", bg= "yellow").pack()

        self.estad_gy= tk.Label(self.uno, text= "Este es el estado de gastos mayores:")
        self.estad_gy.pack()
        
        self.espac= tk.Label(self.uno, text= "", bg= "yellow").pack()

        self.table_1= tk.LabelFrame(self.uno, bd= 0)
        self.table_1.pack()

        if True: # La Tabla
            
            self.aport_1= tk.Label(self.table_1, text= "Aporte obligatorio a la Casa:")
            self.aport_1.grid(row= 0, column= 0)
            
            self.aport_2= tk.Label(self.table_1, text= "Aporte flexible a la Casa:")
            self.aport_2.grid(row= 1, column= 0)

            self.espac_table= tk.Label(self.table_1, text= "")
            self.espac_table.grid(row= 2, column= 0)

            self.total_1= tk.Label(self.table_1, text= "El aporte total es:")
            self.total_1.grid(row= 3, column= 0)

        if True: # Los valores
            
            self.gast_11= tk.Label(self.table_1, text= self.gasta_1[1])
            self.gast_11.grid(row= 0, column= 1)

            self.gast_12= tk.Label(self.table_1, text= self.gasta_2[1])
            self.gast_12.grid(row= 1, column= 1)

            suma_g1= self.gasta_1[1] + self.gasta_2[1]

            self.gast_13= tk.Label(self.table_1, text= suma_g1)
            self.gast_13.grid(row= 3, column= 1)

        "............................................."

        self.espac= tk.Label(self.dos, text= "", bg= "red").pack()

        self.estad_gn= tk.Label(self.dos, text= "Este es el estado de gastos menores:")
        self.estad_gn.pack()
        
        self.espac= tk.Label(self.dos, text= "", bg= "red").pack()

        self.table_2= tk.LabelFrame(self.dos, bd= 0)
        self.table_2.pack()

        if True: # La Tabla
                        
            self.pbsp= tk.Label(self.table_2, text= "En prods basicos de salud pers:")
            self.pbsp.grid(row= 0, column= 0)
            
            self.ppm= tk.Label(self.table_2, text= "un (1) producto para Mi:")
            self.ppm.grid(row= 1, column= 0)

            self.vph= tk.Label(self.table_2, text= "un Valor para el ahorro:")
            self.vph.grid(row= 2, column= 0)

            self.espac_tabla= tk.Label(self.table_2, text= "")
            self.espac_tabla.grid(row= 3, column= 0)

            self.total_2= tk.Label(self.table_2, text= "El aporte total es:")
            self.total_2.grid(row= 4, column= 0)

        if True: # Los valores
            
            self.gast_21= tk.Label(self.table_2, text= self.gasta_3[1])
            self.gast_21.grid(row= 0, column= 1)

            self.gast_22= tk.Label(self.table_2, text= self.gasta_4[1])
            self.gast_22.grid(row= 1, column= 1)

            self.gast_23= tk.Label(self.table_2, text= self.gasta_5[1])
            self.gast_23.grid(row= 2, column= 1)

            suma_g2= self.gasta_3[1] + self.gasta_4[1] + self.gasta_5[1]

            self.gast_24= tk.Label(self.table_2, text= suma_g2)
            self.gast_24.grid(row= 4, column= 1)

        "............................................."

        self.prim_edicion= False

        self.edit_gast= tk.Button(self.gastos, text= "¿Deseas editar?", height= 2, bg= "blue", command= self.edit_gastos)
        self.edit_gast.pack(fill= tk.X, side= "bottom")

        self.conti_nu= tk.Button(self.gastos, text= "Continuar", height= 2, bg= "orange", command= self.cuenta_2)
        self.conti_nu.pack(fill= tk.X, side= "bottom")
        
        self.ya_a_gastos_m= True
        
        
    def operacion_2(self):
        
        if self.ya_a_gastos_m == False:
            self.extrae_db_gasto()
        
        self.operacion_gastos()
        
        activ_1= self.text_4.get()
        activ_2= self.text_5.get()
        
        suma= int(activ_1) + int(activ_2)
        
        self.primera_variable -= suma
        
        self.cuenta_3()
    
    def cuenta_2(self):

        self.world_1.forget()
        self.gastos.forget()
        self.world_2.pack()

        self.separeit_6= tk.Label(self.world_2, text= "").pack()

        self.eficascia= tk.Label(self.world_2, text= "¿Cuanto ha invertido en hacer eficaz tu adquisicion de activos?")
        self.eficascia.pack()
        
        self.text_4= tk.Entry(self.world_2)
        self.text_4.pack()
        
        self.separeit_7= tk.Label(self.world_2, text= "").pack()

        self.depositado= tk.Label(self.world_2, text= "¿Cuanto has depositada en activos recientemente?")
        self.depositado.pack()
        
        self.text_5= tk.Entry(self.world_2)
        self.text_5.pack()

        self.separeit_8= tk.Label(self.world_2, text= "").pack()

        self.conti_qut= tk.LabelFrame(self.world_2)
        self.conti_qut.pack()

        self.contiacti= tk.Button(self.conti_qut, text= "continuar", padx= 50, pady= 35, command= self.operacion_2)
        self.contiacti.pack()

    def cuenta_3(self):
        
        self.world_2.forget()
        self.world_3.pack()
    
        self.ladoizq= tk.LabelFrame(self.world_3)
        self.ladoizq.grid(row= 0, column= 0)
        self.ladocent= tk.LabelFrame(self.world_3)
        self.ladocent.grid(row= 0, column= 1)
        self.ladoder= tk.LabelFrame(self.world_3)
        self.ladoder.grid(row= 0, column= 2)
        
        "........................................."
        
        self.colchon_de_cambio= tk.Label(self.ladoizq, text= "El colchon esta en:")
        self.colchon_de_cambio.pack()
        
        self.dato_5= tk.Entry(self.ladoizq)
        self.dato_5.pack()
        
        self.separeit_6= tk.Label(self.ladoizq, text= "").pack()

        self.el_valor_colchon= tk.Label(self.ladoizq, text= "¿Se ha completado su ahorro?")
        self.el_valor_colchon.pack()
        
        self.dato_6= tk.Entry(self.ladoizq)
        self.dato_6.pack()
                
        "........................................."

        self.activos= tk.Label(self.ladocent, text= "¿Cuantos activos tienes en posecion?")
        self.activos.pack()
        
        self.dato_7= tk.Entry(self.ladocent)
        self.dato_7.pack()

        self.acti_plat= tk.Label(self.ladocent, text= "Nombra en que plataformas se encuentran:")
        self.acti_plat.pack()

        self.dato_8= tk.Text(self.ladocent)
        self.dato_8.pack()

        "........................................."

        self.final= tk.Button(self.ladoizq, text= "Resultados", padx= 30, pady= 40, background= "yellow", command= self.cuenta_4)
        self.final.pack()
        
    def operacion_4(self):
        
        texto= self.text_6.get()
        txop= int(texto)
                
        resto= self.primera_variable - txop
        porcient= resto / self.primera_variable
        
        valor= int(porcient * 100)
        self.algaret_2["text"]= str(valor) + "%"
        
        if valor < 70:
            self.algaret_3["text"]= "(ojo con esa cantidad)"
        else:
            self.algaret_3["text"]= ""
    
    def cuenta_4(self):
            
        respu= self.dato_6.get()
        res= respu.lower()
        
        if (res == "yes") or (res == "si"):
            self.se_ha_completado_el_ahorro= True

        if self.se_ha_completado_el_ahorro == True:
        
            self.world_3.forget()
            self.world_4.pack()
            
            self.separeit_9= tk.Label(self.world_4, text= "").pack()

            self.detodolo_anterior= tk.Label(self.world_4, text= "De todo lo anterior te quedan {}".format(self.primera_variable))
            self.detodolo_anterior.pack()

            self.separeit_9= tk.Label(self.world_4, text= "").pack()

            self.algaret= tk.Label(self.world_4, text= "para tu algarete personal... ¿Cuanto piensas usar?")
            self.algaret.pack()
            
            self.text_6= tk.Entry(self.world_4)
            self.text_6.pack()
            
            self.separeit_9= tk.Label(self.world_4, text= "").pack()

            self.cuadro= tk.LabelFrame(self.world_4, bd= 0)
            self.cuadro.pack()

            self.algaret_0= tk.Label(self.cuadro, text= "Lo que le queda en porcentaje del... algarete es:")
            self.algaret_0.grid(row= 0, column= 0)
            
            self.algaret_1= tk.Button(self.cuadro, text= "procesa", padx= 5, command= self.operacion_4)
            self.algaret_1.grid(row= 0, column= 1)
            
            self.algaret_2= tk.Label(self.cuadro, text= "")
            self.algaret_2.grid(row= 0, column= 2)

            self.algaret_3= tk.Label(self.cuadro, text= "")
            self.algaret_3.grid(row= 0, column= 3)

            self.separeit_9= tk.Label(self.world_4, text= "").pack()

            self.algaret= tk.Label(self.world_4, text= "¿Recibes algo de Rotacion de algun negocio, Dime cuanto por favor?")
            self.algaret.pack()
            
            self.text_8= tk.Entry(self.world_4)
            self.text_8.pack()
            
            self.separeit_9= tk.Label(self.world_4, text= "").pack()

            self.de_res= tk.LabelFrame(self.world_4)
            self.de_res.pack()
            
            self.a_resul= tk.Button(self.de_res, text= "Saliendo", padx= 60, pady= 30, command= self.resultado)
            self.a_resul.pack()
         
        else:
            self.cuenta_3()

    def resultado(self):
        
        self.world_4.forget()
        self.resultados.pack()

        self.mensgfinal= tk.Label(self.resultados, text= "\nRecuerda consumir lo menos posible\n\
            mantenerte bien de ropa y conseguir... \n\
            Una casa\n\
            Un taller\n\
            {} \n\n\n\n\
            Tambien recuerda que las inversiones pueden ser de:\n\
            Copytrade\n\
            Fondos de inversion\n\
            CDTs\n\
            Y que sus mejores rendimientos son del:\n\
            10% y el 15%\n\n\
            Si te queda algo de tu algarete, deberias usarlo para inversion".format(self.gusto_por_profesion))
        self.mensgfinal.pack()
        
