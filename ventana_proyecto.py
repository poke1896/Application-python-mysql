from lib2to3.pytree import Leaf
from tkinter import *
from tkinter import ttk
from coneccion import *
from tkinter import messagebox




class proyecto(Frame):

    usuarios = conec()
#codigo para el identificador master y llamado de funciones 
    def __init__(self, master=None):
        super().__init__(master,width=1153, height=260,background="black")
        self.master = master
        self.pack()
        self.create_widgets()
        
       
       
       
       
# Limpia la cajas de texto cada vez que es llamdo
    
        
# Limpia la el grid lo cual lo recorre econ un for .delete
    def limpiaGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)

        for item in self.grid.get_children():
                self.grid2.delete(item)

# llena el grid con un insert 
    def llenarDatos(self):
        datos = self.usuarios.consulta_proyecto_empleado()
        for row in datos:
            self.grid.insert("",END,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]), tags=('LOL'))
        
        if len(self.grid.get_children()) > 0:
            self.grid.selection_set(self.grid.get_children()[0])

    def llenarDatos2(self):
        datos2 = self.usuarios.consulta_persona_voluntario()
        for row2 in datos2:
            self.grid2.insert("",END,text=row2[0],values=(row2[1],row2[2],row2[3],row2[4],row2[5],row2[6]), tags=('LOL'))
        
        if len(self.grid2.get_children()) > 0:
            self.grid2.selection_set(self.grid2.get_children()[0])

    
    

#activan los combobox mientras se van introduciendo los datos
   
    def create_widgets(self):
        frame1 = Frame(self, bg="#283747")
        frame1.place(x=0,y=0,width=92, height=259)   
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('Treeview.Heading', background="#808B96",foreground='black')
        
        

        self.btnNuevo=Button(frame1,text="Empleado",command= self.create_widgets_proyecto1, bg="#283747", fg="white")
        self.btnNuevo.place(x=0,y=0,width=92, height=30 )        
        self.btnModificar=Button(frame1,text="Voluntario",command= self.create_widgets_proyecto2, compound=self.grid_remove(),  bg="#283747", fg="white")
        self.btnModificar.place(x=0,y=30,width=92, height=30)                
       
    def create_widgets_proyecto1(self):       
        
        frame3 = Frame(self, bg= "black")    
        frame3.place(x=99,y=0,width=998, height=259)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
            background="black",
            foreground="black",
            rowheight=25,
            fieldbackground="black")
        

        self.grid = ttk.Treeview(frame3, columns=("col1","col2","col3","col4","col5","col6","col7","col8"))        
        self.grid.column("#0",width=80)
        self.grid.tag_configure('LOL',background='black',foreground='white')
        self.grid.column("col1",width=100, anchor=CENTER)
        self.grid.column("col2",width=90, anchor=CENTER)
        self.grid.column("col3",width=110, anchor=CENTER)
        self.grid.column("col4",width=90, anchor=CENTER)     
        self.grid.column("col5",width=140, anchor=CENTER)
        self.grid.column("col6",width=90, anchor=CENTER)
        self.grid.column("col7",width=180, anchor=CENTER)
        self.grid.column("col8",width=90, anchor=CENTER)      
        self.grid.heading("#0", text="id_empleado", anchor=CENTER)
        self.grid.heading("col1", text="Nombre", anchor=CENTER)
        self.grid.heading("col2", text="Primer Apellido", anchor=CENTER)
        self.grid.heading("col3", text="Segundo Apellido", anchor=CENTER)
        self.grid.heading("col4", text="puesto", anchor=CENTER)
        self.grid.heading("col5", text="Nombre_Proyecto", anchor=CENTER)
        self.grid.heading("col6", text="Gasto", anchor=CENTER)
        self.grid.heading("col7", text="Obejtivo", anchor=CENTER)
        self.grid.heading("col8", text="monto", anchor=CENTER)
    
         

        self.grid.pack(side=LEFT, fill = Y)

        sb=Scrollbar(frame3, orient=VERTICAL)
        sb.pack(side=RIGHT, fill = Y)
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)
        
        self.grid['selectmode']='browse'
        self.llenarDatos()

    def create_widgets_proyecto2(self):       
        
        
        frame4 = Frame(self, bg= "black")    
        frame4.place(x=99,y=0,width=812, height=259)
        frame9 = Frame(self, bg= "black")    
        frame9.place(x=895,y=0,width=250, height=259)

        style2 = ttk.Style()
        style2.theme_use("clam")
        style2.configure("Treeview",
            background="black",
            foreground="black",
            rowheight=25,
            fieldbackground="black")
    

        self.grid2 = ttk.Treeview(frame4, columns=("col1","col2","col3","col4","col5","col6"))        
        self.grid2.column("#0",width=80)
        self.grid2.tag_configure('LOL',background='black',foreground='white')
        self.grid2.column("col1",width=100, anchor=CENTER)
        self.grid2.column("col2",width=90, anchor=CENTER)
        self.grid2.column("col3",width=110, anchor=CENTER)
        self.grid2.column("col4",width=140, anchor=CENTER)     
        self.grid2.column("col5",width=180, anchor=CENTER)
        self.grid2.column("col6",width=90, anchor=CENTER)
        self.grid2.heading("#0", text="id_empleado", anchor=CENTER)
        self.grid2.heading("col1", text="Nombre", anchor=CENTER)
        self.grid2.heading("col2", text="Primer Apellido", anchor=CENTER)
        self.grid2.heading("col3", text="Segundo Apellido", anchor=CENTER)
        self.grid2.heading("col4", text="Nombre_Proyecto", anchor=CENTER)
        self.grid2.heading("col5", text="Objetivo", anchor=CENTER)
        self.grid2.heading("col6", text="gasto", anchor=CENTER)


        self.grid2.pack(side=LEFT, fill = Y)

        sb2=Scrollbar(frame4, orient=VERTICAL)
        sb2.pack(side=RIGHT, fill = Y)
        self.grid2.config(yscrollcommand=sb2.set)
        sb2.config(command=self.grid2.yview)

        self.grid2['selectmode']='browse'
        self.llenarDatos2()