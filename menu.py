from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from  ventana_persona import Persona
from  ventana_df import DF
from  ventana_rh import RH
from ventana_proyecto import proyecto
from ventana_administrativo import Administrativo

class Menu1():
        
    def __init__(self, window):
       
        self.window = window
        
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Login Page')
        self.create_widgets()


    
    def ventana_open_rh(self):
        root = Tk()
        root.wm_title("RH")
        root.configure(background='black')
        app = RH(root) 
        app.mainloop()

    def ventana_open_persona(self):
        root = Tk()
        root.wm_title("Practica")
        root.configure(background='black')
        app = Persona(root) 
        app.mainloop()

    def ventana_open_cliente(self):
        root = Tk()
        root.wm_title("Practica")
        root.configure(background='black')
        app = Persona(root) 
        app.mainloop()

    def ventana_open_proyecto(self):
        root = Tk()
        root.wm_title("Practica")
        root.configure(background='black')
        app = proyecto(root) 
        app.mainloop()

    def ventana_open_df(self):
        root = Tk()
        root.wm_title("Practica")
        root.configure(background='black')
        app = DF(root) 
        app.mainloop()

    def ventana_open_administrativo(self):
        root = Tk()
        root.wm_title("Practica")
        root.configure(background='black')
        app = Administrativo(root) 
        app.mainloop()

    def create_widgets(self):  
        # ========================================================================
        # ============================background image============================
        # ========================================================================
        
        # ====== Login Frame =========================
        self.menu_frame = Frame(self.window, bg='#040405', width=950, height=600)
        self.menu_frame.place(x=200, y=70)
        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "Bienvenido a Menu"
        self.heading = Label(self.menu_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=80, y=30, width=500, height=50)

        # ========================================================================
        self.menu_rh_button = Image.open('images\\btnmenu.png')
        photo = ImageTk.PhotoImage(self.menu_rh_button)
        self.menu_rh_button_label = Label(self.menu_frame, image=photo, bg='#040405')
        self.menu_rh_button_label.image = photo
        self.menu_rh_button_label.place(x=30, y=110)
        self.rh = Button(self.menu_rh_button_label, text='Recursos Humanos', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command=self.ventana_open_rh)
        self.rh.place(x=20, y=10)
        # ==============================
        # ========================================================================
        self.menu_persona_button = Image.open('images\\btnmenu.png')
        photo = ImageTk.PhotoImage(self.menu_persona_button)
        self.menu_persona_button_label = Label(self.menu_frame, image=photo, bg='#040405')
        self.menu_persona_button_label.image = photo
        self.menu_persona_button_label.place(x=30, y=180)
        self.persona = Button(self.menu_persona_button_label, text='Persona', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command = self.ventana_open_persona)
        self.persona.place(x=20, y=10)
        # ==============================
       
        # ========================================================================
        self.menu_cliente_button = Image.open('images\\btnmenu.png')
        photo = ImageTk.PhotoImage(self.menu_cliente_button)
        self.menu_cliente_button_label = Label(self.menu_frame, image=photo, bg='#040405')
        self.menu_cliente_button_label.image = photo
        self.menu_cliente_button_label.place(x=30, y=250)
        self.clientes = Button(self.menu_cliente_button_label, text='Clientes', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
        self.clientes.place(x=20, y=10)
        # ==============================
        # ========================================================================
        self.menu_depfinanzas_button = Image.open('images\\btnmenu.png')
        photo = ImageTk.PhotoImage(self.menu_depfinanzas_button)
        self.menu_depfinanzas_button_label = Label(self.menu_frame, image=photo, bg='#040405')
        self.menu_depfinanzas_button_label.image = photo
        self.menu_depfinanzas_button_label.place(x=30, y=320)
        self.df = Button(self.menu_depfinanzas_button_label, text='Dep.Finanzas', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=self.ventana_open_df)
        self.df.place(x=20, y=10)
        # ==============================
        # ========================================================================
        self.menu_crear_button = Image.open('images\\btnverde.png')
        photo = ImageTk.PhotoImage(self.menu_crear_button)
        self.menu_crear_button_label = Label(self.menu_frame, image=photo, bg='#040405')
        self.menu_crear_button_label.image = photo
        self.menu_crear_button_label.place(x=30, y=410)
        self.crear = Button(self.menu_crear_button_label, text='Crear base datos', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#93c47d', cursor='hand2', activebackground='#93c47d', fg='white')
        self.crear.place(x=20, y=10)
        # ==============================
        # ========================================================================
        self.menu_eliminar_button = Image.open('images\\btnred.png')
        photo = ImageTk.PhotoImage(self.menu_eliminar_button)
        self.menu_eliminar_button_label = Label(self.menu_frame, image=photo, bg='#040405')
        self.menu_eliminar_button_label.image = photo
        self.menu_eliminar_button_label.place(x=30, y=480)
        self.borrar = Button(self.menu_eliminar_button_label, text='Eliminar base datos', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#a10000', cursor='hand2', activebackground='#a10000', fg='white')
        self.borrar.place(x=20, y=10)
        # ==============================
        # ========================================================================
        self.menu_mercadeo_button = Image.open('images\\btnmenu.png')
        photo = ImageTk.PhotoImage(self.menu_mercadeo_button)
        self.menu_mercadeo_button_label = Label(self.menu_frame, image=photo, bg='#040405')
        self.menu_mercadeo_button_label.image = photo
        self.menu_mercadeo_button_label.place(x=400, y=110)
        self.gasto = Button(self.menu_mercadeo_button_label, text='Dep_Administrativo', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=self.ventana_open_administrativo)
        self.gasto.place(x=20, y=10)
        # ==============================
        # ========================================================================
        self.menu_proyecto_button = Image.open('images\\btnmenu.png')
        photo = ImageTk.PhotoImage(self.menu_proyecto_button)
        self.menu_proyecto_button_label = Label(self.menu_frame, image=photo, bg='#040405')
        self.menu_proyecto_button_label.image = photo
        self.menu_proyecto_button_label.place(x=400, y=180)
        self.proyecto = Button(self.menu_proyecto_button_label, text='Proyecto', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=self.ventana_open_proyecto)
        self.proyecto.place(x=20, y=10)
        # ==============================
