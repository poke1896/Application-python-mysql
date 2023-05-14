import mysql.connector

class Registro_datos():

    def __init__(self):
        self.conexion = mysql.connector.connect(host="localhost",
                                                database = "loginpass",
                                                user= "root",
                                                password= "1896"
                                                )
    def buscar_users(self,users):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM login_datos where Users = '{}'".format(users)
        cur.execute(sql)
        usersx=cur.fetchall()
        
        cur.close()
        return usersx

    def buscar_password(self,password):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM login_datos where Password = '{}'".format(password)
        cur.execute(sql)
        passwordx=cur.fetchall()
        
        cur.close()
        return passwordx

