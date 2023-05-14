from lib2to3.pytree import Leaf
from tkinter import *
from tkinter import ttk
from coneccion import *
from tkinter import messagebox




class Persona(Frame):

    conec = conec()
#codigo para el identificador master y llamado de funciones 
    def __init__(self, master=None):
        super().__init__(master,width=1930, height=610,background="black")
        self.master = master
        self.pack()
        self.create_widgets()
        self.llenarDatos()
        self.habilitarCajas("disabled")
        self.habilitarBtnOper("normal")
        self.habilitarBtnAct("disable")
        self.habilitarComboBoxCanton("disabled")
        self.habilitarComboBoxDistrito("disabled")
        self.habilitarComboBoxProvincia("disabled")
        self.id_usuario=-1
       
    
#habilita las cajas de texto
    def habilitarCajas(self, estado):
        self.txtNombre.configure(state=estado)
        self.txtapellido.configure(state=estado)
        self.txtsegApellido.configure(state=estado)
        self.txttelefono.configure(state=estado)
#habilita los botones de operaciones costado izquierdo 
    def habilitarBtnOper(self, estado):
        self.btnNuevo.configure(state=estado)
        self.btnModificar.configure(state=estado)
        self.btnEliminar.configure(state=estado)
#habilita los botones de actividades costado abajo de caja de textos 
    def habilitarBtnAct(self, estado):
        self.btnGuardar.configure(state=estado)
        self.btnCancelar.configure(state=estado)
#habilita las cajas comboboxes  
    def habilitarComboBoxProvincia(self, estado):
       self.btnProvincia.configure(state=estado)
       self.comboboxProvincia.configure(state=estado)
        
    def habilitarComboBoxCanton(self, estado):
       self.btnCanton.configure(state=estado)
       self.comboboxCanton.configure(state=estado)
    
    def habilitarComboBoxDistrito(self, estado):
       self.btnDistrito.configure(state=estado)
       self.comboboxDistrito.configure(state=estado)
       
       
       
# Limpia la cajas de texto cada vez que es llamdo
    def limpiarCajas(self):
        self.txtNombre.delete(0,END)
        self.txtapellido.delete(0,END)
        self.txtsegApellido.delete(0,END)
        self.txttelefono.delete(0,END)
        
# Limpia la el grid lo cual lo recorre econ un for .delete
    def limpiaGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)

# llena el grid con un insert 
    def llenarDatos(self):
        datos = self.conec.consulta_persona()
        for row in datos:
            self.grid.insert("",END,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16]), tags=('LOL'))
        
        if len(self.grid.get_children()) > 0:
            self.grid.selection_set(self.grid.get_children()[0])

    
    def llenarDatosProvincia(self):
        datos = self.conec.consulta_Provincia()
        resultProvincia=[]
        
        for row in datos:
            resultProvincia.append( row[1])

        return resultProvincia

    

 # recive el dato selecionado y le da una cave, este dato lo manda a un join para recivir el canton       
    def llenarDatosCanton(self):
        Provincia = self.comboboxProvincia.get()
        
       
        claves = 0
        if Provincia == "San José":
            claves = 1

        if Provincia == "Alajuela":
            claves = 2

        if Provincia == "Cartago":
            claves = 3

        if Provincia == "Heredia":
            claves = 4
             
        if Provincia == "Guanacaste":
            claves = 5
            
        if Provincia == "Puntarenas":
            claves = 6
            
        if Provincia == "Limón":
            claves = 7
            

        datos = self.conec.consulta_Canton(claves)

        resultCanton=[]
        
        for row in datos:
            resultCanton.append(row[0])
        return resultCanton

    
## recive el dato del combox y lo envia a join distrito para sacarlo
    def llenarDatosDistrito(self):
        canton = self.comboboxCanton.get()
        

        datos = self.conec.consulta_Distrito(canton)
    
        resultDistrito=[]
        
        for row in datos:
            resultDistrito.append(row[0])
        return resultDistrito
  


            
    #habilita caja de texto y botnes act bloqueando el de operaciones
    def fNuevo(self): 
       
        self.habilitarCajas("normal")
        self.habilitarBtnOper("disabled")  
        self.habilitarBtnAct("normal") 
        self.btnGuardar.config(state="disabled") 
        self.habilitarComboBoxProvincia("normal") 
        self.limpiarCajas()
        self.txtNombre.focus()
       
    #desabilita los botens de accion y habilita los de operaciones ademas que envia los datos de las cajas de texto y combobox sea a incertar cliente o a modificar clientes
    def fGuardar(self):       
        if self.id_usuario == -1:
            self.conec.inserta_cliente(self.txtNombre.get(),self.txtapellido.get(),self.txtsegApellido.get(),self.txttelefono.get(),self.comboboxProvincia.get(),self.comboboxCanton.get(),self.comboboxDistrito.get())
            messagebox.showinfo("Insertar","Elemento Insertado correctamente.")
            
          
        else:
            self.conec.modifica_cliente(self.id_usuario,self.txtNombre.get(),self.txtapellido.get(),self.txtsegApellido.get(),self.txttelefono.get(),self.comboboxProvincia.get(),self.comboboxCanton.get(),self.comboboxDistrito.get())
            messagebox.showinfo("Modificar","Elemento Modificado correctamente.")
            self.id_usuario = -1


        self.limpiaGrid()
        self.llenarDatos()
        self.limpiarCajas()
        self.habilitarBtnAct("disabled")
        self.habilitarBtnAct("disabled")
        self.habilitarBtnOper("normal")            
        self.habilitarComboBoxDistrito("disabled")
        self.habilitarCajas("disabled")
        
# optiene los datos del grid selecionados y los pone en la caja de texto 
    def fModificar(self):        
        selected = self.grid.focus()
        clave = self.grid.item(selected,'text')
        if clave=='':
            messagebox.showwarning("Modificar","Debes seleccionar un elemento.")
            
        else:
            self.txtNombre.focus()

            self.id_usuario = clave
            self.habilitarCajas("normal")
            valores = self.grid.item(selected,'values')
            self.limpiarCajas()
            
            self.txtNombre.insert(0,valores[0])
            self.txtapellido.insert(0,valores[1])
            self.txtsegApellido.insert(0,valores[2])
            self.txttelefono.insert(0,valores[3])
            
            self.habilitarComboBoxProvincia("normal") 
            self.habilitarBtnOper("disabled")  
            self.habilitarBtnAct("normal") 
            self.txtNombre.focus()


          
#  le envia los datos del grid y los envia a elimina_cliente
    def fEliminar(self):
        selected = self.grid.focus()
        clave = self.grid.item(selected,'text')
        print(clave)
        if clave=='':
            messagebox.showwarning("Eliminar","Debes seleccionar un elemento.")
            
        else:
            valores = self.grid.item(selected,'values')
            data = str(clave) +", " + valores[0] + ", " + valores[1]
            r = messagebox.askquestion("Eliminar","Deseas eliminar el registro seleccionado?\n" + data)

            if r==messagebox.YES:
                n = self.conec.elimina_cliente(clave)
                m = self.conec.elimina_cliente(clave)
                x = self.conec.elimina_cliente(clave)

                if n != 0:
                    messagebox.showinfo("Eliminar","Elemento eliminado correctamente.")
                    self.limpiaGrid()
                    self.llenarDatos()
                else:
                    messagebox.showinfo("Eliminar","No fue posible eliminar el elemento.")
          

    def fCancelar(self):
         r = messagebox.askquestion("Cancaelar","Estas Seguro que deseas cancelar la operacion actual?")
         if r== messagebox.YES:
            self.limpiarCajas()
            self.habilitarBtnAct("disabled")
            self.habilitarBtnAct("disabled")
            self.habilitarBtnOper("normal")    
        

#activan los combobox mientras se van introduciendo los datos
    def fAcpetarProvincia(self):
        self.habilitarComboBoxCanton("normal")
        self.llenarDatosCanton()
        self.comboboxCanton['value'] = self.llenarDatosCanton()
        self.habilitarComboBoxProvincia("disabled")
        

    def fAcpetarCanton(self):
        self.habilitarComboBoxDistrito("normal")
        self.llenarDatosDistrito()
        self.comboboxDistrito['value'] = self.llenarDatosDistrito()
        self.habilitarComboBoxCanton("disabled")

    def fAcpetarDistrito(self):
        self.btnGuardar.config(state="normal") 
        self.habilitarComboBoxDistrito("disabled")
        pass
    
    def changeOnHover(button, colorOnHover, colorOnLeave): 
  
    
    
     button.bind("<Enter>", func=lambda e: button.config( 
        background=colorOnHover)) 
  
    
     button.bind("<Leave>", func=lambda e: button.config( 
        background=colorOnLeave)) 

    def create_widgets(self):
        frame1 = Frame(self, bg="#283747")
        frame1.place(x=0,y=0,width=93, height=610)   
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('Treeview.Heading', background="#808B96",foreground='black')

        self.btnNuevo=Button(frame1,text="Nuevo", command=self.fNuevo, bg="#283747", fg="white")
        self.btnNuevo.place(x=0,y=0,width=92, height=30 )        
        self.btnModificar=Button(frame1,text="Modificar", command=self.fModificar, bg="#283747", fg="white")
        self.btnModificar.place(x=0,y=30,width=92, height=30)                
        self.btnEliminar=Button(frame1,text="Eliminar", command=self.fEliminar, bg="#283747", fg="white")
        self.btnEliminar.place(x=0,y=60,width=92, height=30)   
            
        frame2 = Frame(self,bg="#808B96" )
        frame2.place(x=94,y=0,width=150, height=610) 
        lbl1 = Label(frame2,text="Cedula: ",bg="#808B96")
        lbl1.place(x=3,y=5)        
        self.txtcedula=Entry(frame2)
        self.txtcedula.place(x=3,y=25,width=135, height=20)  

        lbl2 = Label(frame2,text="Nombre: ",bg="#808B96")
        lbl2.place(x=3,y=55)        
        self.txtNombre=Entry(frame2)
        self.txtNombre.place(x=3,y=75,width=135, height=20)

        lbl3 = Label(frame2,text="Primer Apellido: ",bg="#808B96")
        lbl3.place(x=3,y=105)        
        self.txtapellido=Entry(frame2)
        self.txtapellido.place(x=3,y=125,width=135, height=20)  

        lbl4 = Label(frame2,text="Segundo Apellido: ",bg="#808B96")
        lbl4.place(x=3,y=155)        
        self.txtsegApellido=Entry(frame2)
        self.txtsegApellido.place(x=3,y=175,width=135, height=20)   

        lbl5 = Label(frame2,text="Telefono: ",bg="#808B96")
        lbl5.place(x=3,y=205)        
        self.txttelefono=Entry(frame2)
        self.txttelefono.place(x=3,y=225,width=135, height=20) 

        lbl6 = Label(frame2,text="Correo: ",bg="#808B96")
        lbl6.place(x=3,y=255)        
        self.txtcorreo=Entry(frame2)
        self.txtcorreo.place(x=3,y=275,width=135, height=20)     

        lbl7 = Label(frame2,text="Fecha de nacimiento: ",bg="#808B96")
        lbl7.place(x=3,y=305)        
        self.txtfecha_n=Entry(frame2)
        self.txtfecha_n.place(x=3,y=325,width=135, height=20)  
                      
        lbl8 = Label(frame2,text="Horas laboradas: ",bg="#808B96")
        lbl8.place(x=3,y=355)        
        self.txthoras=Entry(frame2)
        self.txthoras.place(x=3,y=375,width=135, height=20)      

        lbl9 = Label(frame2,text="Salario: ",bg="#808B96")
        lbl9.place(x=3,y=405)        
        self.txtsalario=Entry(frame2)
        self.txtsalario.place(x=3,y=425,width=135, height=20) 

        lbl10 = Label(frame2,text="Evalucacion: ",bg="#808B96")
        lbl10.place(x=3,y=455)        
        self.txtevaluacion=Entry(frame2)
        self.txtevaluacion.place(x=3,y=475,width=135, height=20) 

        lbl11 = Label(frame2,text="Fecha de pago: ",bg="#808B96")
        lbl11.place(x=3,y=505)        
        self.txtfecha_p=Entry(frame2)
        self.txtfecha_p.place(x=3,y=525,width=135, height=20)  

          

        self.btnGuardar=Button(frame2,text="Guardar", command=self.fGuardar, bg="green", fg="white")
        self.btnGuardar.place(x=10,y=575,width=60, height=30)
        self.btnCancelar=Button(frame2,text="Cancelar", command=self.fCancelar, bg="red", fg="white")
        self.btnCancelar.place(x=80,y=575,width=60, height=30)  

        frame3 = Frame(self, bg= "black")    
        frame3.place(x=392,y=0,width=1529, height=259)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
            background="black",
            foreground="black",
            rowheight=25,
            fieldbackground="black")
        

        #style.map('Treeview', 
            #background[('selected','white')])

        self.grid = ttk.Treeview(frame3, columns=("col1","col2","col3","col4","col5","col6","col7","col8","col9","col10","col11","col12","col13","col14","col15","col16"))        
        self.grid.column("#0",width=50)
        self.grid.tag_configure('LOL',background='black',foreground='white')
        self.grid.column("col1",width=100, anchor=CENTER)
        self.grid.column("col2",width=90, anchor=CENTER)
        self.grid.column("col3",width=110, anchor=CENTER)
        self.grid.column("col4",width=90, anchor=CENTER)     
        self.grid.column("col5",width=90, anchor=CENTER)
        self.grid.column("col6",width=90, anchor=CENTER)
        self.grid.column("col7",width=90, anchor=CENTER)    
        self.grid.column("col8",width=90, anchor=CENTER)    
        self.grid.column("col9",width=80, anchor=CENTER)    
        self.grid.column("col10",width=90, anchor=CENTER)    
        self.grid.column("col11",width=90, anchor=CENTER)    
        self.grid.column("col12",width=90, anchor=CENTER)    
        self.grid.column("col13",width=90, anchor=CENTER)   
        self.grid.column("col14",width=90, anchor=CENTER)    
        self.grid.column("col15",width=90, anchor=CENTER)     
        self.grid.column("col16",width=90, anchor=CENTER)    
             
        
        self.grid.heading("#0", text="id_persona", anchor=CENTER)
        self.grid.heading("col1", text="Cedula", anchor=CENTER)
        self.grid.heading("col2", text="Nombre", anchor=CENTER)
        self.grid.heading("col3", text="Primer Apellido", anchor=CENTER)
        self.grid.heading("col4", text="Segundo Apellido", anchor=CENTER)
        self.grid.heading("col5", text="Telefono", anchor=CENTER)
        self.grid.heading("col6", text="Telefono", anchor=CENTER)
        self.grid.heading("col7", text="Provincia", anchor=CENTER)
        self.grid.heading("col8", text="Canton", anchor=CENTER)
        self.grid.heading("col9", text="Distrito", anchor=CENTER)
        self.grid.heading("col10", text="fecha de nacimiento", anchor=CENTER)
        self.grid.heading("col11", text="Cedula", anchor=CENTER)
        self.grid.heading("col12", text="Nombre", anchor=CENTER)
        self.grid.heading("col13", text="Primer Apellido", anchor=CENTER)
        self.grid.heading("col14", text="Segundo Apellido", anchor=CENTER)
        self.grid.heading("col15", text="Parentesco", anchor=CENTER)
        self.grid.heading("col16", text="fecha de nacimiento", anchor=CENTER) 
        

    
        frame4 = Frame(self,bg="#808B96" )
        frame4.place(x=240,y=0,width=151, height=84) 

        frame5 = Frame(self,bg="#808B96" )
        frame5.place(x=240,y=84,width=151, height=90)

        frame6 = Frame(self,bg="#808B96" )
        frame6.place(x=240,y=174,width=151, height=610)


        lbl5 = Label(frame4,text="Provincia: ",bg="#808B96")
        lbl5.place(x=3,y=5) 
        self.comboboxProvincia = ttk.Combobox(frame4,width=120, height=20,state="readonly")      
        self.comboboxProvincia.set("Provincia")
        self.comboboxProvincia['value'] = self.llenarDatosProvincia()
        self.comboboxProvincia.pack(padx = 3, pady = 30)
        self.btnProvincia=Button(frame4,text="Aceptar", command=self.fAcpetarProvincia, bg="#283747", fg="white")
        self.btnProvincia.place(x=3,y=56,width=50, height=20)
        

        lbl6 = Label(frame5,text="Canton: ",bg="#808B96")
        lbl6.place(x=3,y=5)        
        self.comboboxCanton = ttk.Combobox(frame5,width=120, height=20,state="readonly") 
        self.comboboxCanton.set("Canton")
        
        self.comboboxCanton.pack(padx = 3, pady = 30) 
        self.btnCanton=Button(frame5,text="Aceptar", command=self.fAcpetarCanton, bg="#283747", fg="white")
        self.btnCanton.place(x=3,y=56,width=50, height=20) 

        lbl7 = Label(frame6,text="Distrito: ",bg="#808B96")
        lbl7.place(x=3,y=5)   
        self.comboboxDistrito = ttk.Combobox(frame6,width=120, height=20,state="readonly") 
        self.comboboxDistrito.set("Distrito")
        
        self.comboboxDistrito.pack(padx = 3, pady = 30) 
        self.btnDistrito=Button(frame6,text="Aceptar", command=self.fAcpetarDistrito, bg="#283747", fg="white")
        self.btnDistrito.place(x=3,y=56,width=50, height=20)   

        self.grid.pack(side=LEFT, fill = Y)

        sb=Scrollbar(frame3, orient=VERTICAL)
        sb.pack(side=RIGHT, fill = Y)
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)

        self.grid['selectmode']='browse'
