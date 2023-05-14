from lib2to3.pytree import Leaf
from tkinter import *
from tkinter import ttk
from coneccion import *
from tkinter import messagebox




class DF(Frame):

    conec = conec()
#codigo para el identificador master y llamado de funciones 
    def __init__(self, master=None):
        super().__init__(master,width=1030, height=500,background="black")
        self.master = master
        self.pack()
        self.create_widgets()
        self.llenarDatos()
        self.llenarDatos2()
    
        
       
        self.id_usuario=-1
       
    
#habilita las cajas de texto

#habilita los botones de operaciones costado izquierdo 

#habilita los botones de actividades costado abajo de caja de textos 
 
#habilita las cajas comboboxes  

       
       
       
# Limpia la cajas de texto cada vez que es llamdo

# Limpia la el grid lo cual lo recorre econ un for .delete
    def limpiaGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)

# llena el grid con un insert 
    def llenarDatos(self):
        datos_ingrsos = self.conec.consulta_ingreso()
        for row in datos_ingrsos:
            self.grid.insert("",END,text=row[0],values=(row[1],row[2]), tags=('LOL'))
        
        if len(self.grid.get_children()) > 0:
            self.grid.selection_set(self.grid.get_children()[0])

        datos_fondos = self.conec.consulta_fondos()
        for row in datos_fondos:
            self.grid2.insert("",END,text=row[0],values=(row[1],row[2]), tags=('LOL'))
            
        if len(self.grid2.get_children()) > 0:
            self.grid2.selection_set(self.grid.get_children()[0])

        datos_gastos = self.conec.consulta_gastos()
        for row in datos_gastos:
            self.grid3.insert("",END,text=row[0],values=(row[1],row[2]), tags=('LOL'))
        
        if len(self.grid3.get_children()) > 0:
            self.grid3.selection_set(self.grid.get_children()[0])

    def llenarDatos2(self):
        datos_ingrsos2 = self.conec.consulta_total_ingreso()
        datos1=str(datos_ingrsos2)
        
        self.txttotal_ingreso.insert(0,datos1)
      
        
        

        datos_fondos2 = self.conec.consulta_total_fondo()  
        datos2=str(datos_fondos2)
        
        self.txttotal_fondo.insert(0,datos2)
            
        

        datos_gastos2 = self.conec.consulta_total_gasto()
        datos3=str(datos_gastos2)
        
        self.txttotal_gasto.insert(0,datos3)
        
       


    

              
        

#activan los combobox mientras se van introduciendo los datos
  

    def create_widgets(self):
        
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('Treeview.Heading', background="#808B96",foreground='black')

        

        frame3 = Frame(self, bg= "black")    
        frame3.place(x=0,y=0,width=353, height=245)
        frame4 = Frame(self, bg= "black")    
        frame4.place(x=353,y=0,width=353, height=245)
        frame5 = Frame(self, bg= "black")    
        frame5.place(x=692,y=0,width=353, height=245)

        frame6 = Frame(self, bg= "#808B96")    
        frame6.place(x=0 ,y=260,width=353, height=245)
        frame7 = Frame(self, bg= "#808B96")    
        frame7.place(x=353,y=260,width=353, height=245)
        frame8 = Frame(self, bg= "#808B96")    
        frame8.place(x=692,y=260,width=353, height=245)

        lbl1 = Label(frame6,text="Monto: ",bg="#808B96")
        lbl1.place(x=3,y=5)        
        self.txtmonto_ingreso=Entry(frame6)
        self.txtmonto_ingreso.place(x=3,y=25,width=135, height=20)  

        lbl2 = Label(frame6,text="Tipo: ",bg="#808B96")
        lbl2.place(x=3,y=55)        
        self.txttipo_ingreso=Entry(frame6)
        self.txttipo_ingreso.place(x=3,y=75,width=135, height=20)
        
        lbl3 = Label(frame7,text="Monto: ",bg="#808B96")
        lbl3.place(x=3,y=5)        
        self.txtmonto_fondo=Entry(frame7)
        self.txtmonto_fondo.place(x=3,y=25,width=135, height=20)  

        lbl4 = Label(frame7,text="Tipo: ",bg="#808B96")
        lbl4.place(x=3,y=55)        
        self.txttipo_fondo=Entry(frame7)
        self.txttipo_fondo.place(x=3,y=75,width=135, height=20)

        lbl5 = Label(frame8,text="monto: ",bg="#808B96")
        lbl5.place(x=3,y=5)        
        self.txtmonto_ingreso=Entry(frame8)
        self.txtmonto_ingreso.place(x=3,y=25,width=135, height=20)
        
        lbl5 = Label(frame8,text="nombre: ",bg="#808B96")
        lbl5.place(x=3,y=55)        
        self.txttipo_ingreso=Entry(frame8)
        self.txttipo_ingreso.place(x=3,y=75,width=135, height=20)
        
        self.btnGuardar_ingreso=Button(frame6,text="Guardar", bg="green", fg="white")
        self.btnGuardar_ingreso.place(x=10,y=125,width=60, height=30)
        self.btnEliminar_ingreso=Button(frame6,text="Eliminar", bg="red", fg="white")
        self.btnEliminar_ingreso.place(x=80,y=125,width=60, height=30)  
        
        self.btnGuardar_fondo=Button(frame7,text="Guardar", bg="green", fg="white")
        self.btnGuardar_fondo.place(x=10,y=125,width=60, height=30)
        self.btnEliminar_fondo=Button(frame7,text="Eliminar", bg="red", fg="white")
        self.btnEliminar_fondo.place(x=80,y=125,width=60, height=30)  

        self.btnGuardar_gasto=Button(frame8,text="Guardar", bg="green", fg="white")
        self.btnGuardar_gasto.place(x=10,y=125,width=60, height=30)
        self.btnEliminar_gasto=Button(frame8,text="Eliminar", bg="red", fg="white")
        self.btnEliminar_gasto.place(x=80,y=125,width=60, height=30)  

        lbl6 = Label(frame6,text="Total de ingresos: ",bg="#808B96")
        lbl6.place(x=3,y=165)  
        lbl7 = Label(frame7,text="Total de fondos: ",bg="#808B96")
        lbl7.place(x=3,y=165)  
        lbl8 = Label(frame8,text="Total de gastos: ",bg="#808B96")
        lbl8.place(x=3,y=165)  
        
        self.txttotal_ingreso=Entry(frame6)
        self.txttotal_ingreso.place(x=3,y=205,width=135, height=20)  
        self.txttotal_fondo=Entry(frame7)
        self.txttotal_fondo.place(x=3,y=205,width=135, height=20)  
        self.txttotal_gasto=Entry(frame8)
        self.txttotal_gasto.place(x=3,y=205,width=135, height=20)  

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
            background="black",
            foreground="black",
            rowheight=25,
            fieldbackground="black")
        




        self.grid = ttk.Treeview(frame3, columns=("col1","col2"))        
        self.grid.column("#0",width=95)
        self.grid.tag_configure('LOL',background='black',foreground='white')
        self.grid.column("col1",width=130, anchor=CENTER)
        self.grid.column("col2",width=110, anchor=CENTER)
       
        self.grid.heading("#0", text="Id dep.Finanzas", anchor=CENTER)
        self.grid.heading("col1", text="Ingresos", anchor=CENTER)
        self.grid.heading("col2", text="Tipo", anchor=CENTER)


        self.grid2 = ttk.Treeview(frame4, columns=("col1","col2"))        
        self.grid2.column("#0",width=95)
        self.grid2.tag_configure('LOL',background='black',foreground='white')
        self.grid2.column("col1",width=130, anchor=CENTER)
        self.grid2.column("col2",width=110, anchor=CENTER)

        self.grid2.heading("#0", text="Id fondos", anchor=CENTER)
        self.grid2.heading("col1", text="Tondos", anchor=CENTER)
        self.grid2.heading("col2", text="Tipo", anchor=CENTER)

        self.grid3 = ttk.Treeview(frame5, columns=("col1","col2"))        
        self.grid3.column("#0",width=95)
        self.grid3.tag_configure('LOL',background='black',foreground='white')
        self.grid3.column("col1",width=130, anchor=CENTER)
        self.grid3.column("col2",width=110, anchor=CENTER)
       
        self.grid3.heading("#0", text="Id gastos", anchor=CENTER)
        self.grid3.heading("col1", text="Tipo", anchor=CENTER)
        self.grid3.heading("col2", text="Monto", anchor=CENTER)



    




        self.grid.pack(side=LEFT, fill = Y)

        sb=Scrollbar(frame3, orient=VERTICAL)
        sb.pack(side=RIGHT, fill = Y)
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)

        self.grid2.pack(side=LEFT, fill = Y)

        sb=Scrollbar(frame4, orient=VERTICAL)
        sb.pack(side=RIGHT, fill = Y)
        self.grid2.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)
        self.grid2['selectmode']='browse'

        self.grid3.pack(side=LEFT, fill = Y)

        sb=Scrollbar(frame5, orient=VERTICAL)
        sb.pack(side=RIGHT, fill = Y)
        self.grid3.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)
        self.grid3['selectmode']='browse'
