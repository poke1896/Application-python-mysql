from lib2to3.pytree import Leaf
from tkinter import *
from tkinter import ttk
from coneccion import *





class Administrativo(Frame):

    conec = conec()
#codigo para el identificador master y llamado de funciones 
    def __init__(self, master=None):
        super().__init__(master,width=800, height=260,background="black")
        self.master = master
        self.pack()
        self.create_widgets()
        self.llenarDatos()

        
# Limpia la el grid lo cual lo recorre econ un for .delete
    def limpiaGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)

# llena el grid con un insert 
    def llenarDatos(self):
        datos = self.conec.consulta_dep_admi()
        for row in datos:
            self.grid.insert("",END,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]), tags=('LOL'))
        
        if len(self.grid.get_children()) > 0:
            self.grid.selection_set(self.grid.get_children()[0])

    


    def create_widgets(self):
           
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('Treeview.Heading', background="#808B96",foreground='black')


        frame3 = Frame(self, bg= "black")    
        frame3.place(x=0,y=0,width=800, height=259)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
            background="black",
            foreground="black",
            rowheight=25,
            fieldbackground="black")
        

        #style.map('Treeview', 
            #background[('selected','white')])

        self.grid = ttk.Treeview(frame3, columns=("col1","col2","col3","col4","col5","col6","col7"))        
        self.grid.column("#0",width=120)
        self.grid.tag_configure('LOL',background='black',foreground='white')
        self.grid.column("col1",width=100, anchor=CENTER)
        self.grid.column("col2",width=90, anchor=CENTER)
        self.grid.column("col3",width=110, anchor=CENTER)
        self.grid.column("col4",width=90, anchor=CENTER)
        self.grid.column("col5",width=110, anchor=CENTER)
        self.grid.column("col6",width=90, anchor=CENTER)  
        self.grid.column("col7",width=90, anchor=CENTER)  

        self.grid.heading("#0", text="Id_Dep_admin", anchor=CENTER)
        self.grid.heading("col1", text="Nombre_Articulo ", anchor=CENTER)
        self.grid.heading("col2", text="Cantidad ", anchor=CENTER)
        self.grid.heading("col3", text="Fecha_ingreso", anchor=CENTER)
        self.grid.heading("col4", text="Fecha_caducidad", anchor=CENTER)
        self.grid.heading("col5", text="Estado", anchor=CENTER)
        self.grid.heading("col6", text="Detalle", anchor=CENTER)
        self.grid.heading("col7", text="Precio", anchor=CENTER)
        

  

        self.grid.pack(side=LEFT, fill = Y)

        sb=Scrollbar(frame3, orient=VERTICAL)
        sb.pack(side=RIGHT, fill = Y)
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)

        self.grid['selectmode']='browse'

def main():
    root = Tk()
    root.wm_title("Practica")
    root.configure(background='black')
    app = Administrativo(root) 
    app.mainloop()



if __name__ == "__main__":
    main()