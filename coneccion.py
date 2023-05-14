import mysql.connector
import re
class conec:

# sirve para hacer la coneccion con la base de datos en local host 
    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root", 
        passwd="1896", database="Base_Datos" )

#hace un selec a provincia recogiendo los datos con un fetchel       
    def consulta_Provincia(self):
        cur = self.cnn.cursor()
        cur.execute("select * from provincia")
        datos = cur.fetchall()
        cur.close()    
        return datos
#hace un selec con un inner join a provincia_canton_detail recogiendo los datos con un fetchel  
    def consulta_Canton(self, ID_Provincia):
        cur = self.cnn.cursor()
        sql=("select C.Canton from Provincia P inner join Provincia_Canton_Detail D ON P.ID_Provincia = D.ID_Provincia inner join Canton C ON D.ID_Canton = C.ID_Canton WHERE P.ID_Provincia = {}").format(ID_Provincia)
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()    
        return datos

    
#hace un selec con un inner join a Canton_Distrito_Detail recogiendo los datos con un fetchel  
    def consulta_Distrito(self, canton):
        cur = self.cnn.cursor()
        sql=("select D.Distrito from Canton C inner join Canton_Distrito_Detail T ON C.ID_Canton = T.ID_Canton inner join Distrito D ON T.ID_Distrito = D.ID_Distrito WHERE C.Canton = '{}' ").format(str(canton))
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()    
        return datos
#hace un selec a cliente con un join inner a usuario_telefono_detail
    def consulta_rh(self):
        cur = self.cnn.cursor()
        cur.execute(" select u.id_empleado,u.cedula,u.nombre, u.primer_apellido, u.segundo_apellido, t.telefono, P.provincia, C.Canton, I.distrito,l.correo,u.fecha_nacimiento,z.horas,z.salario,e.evaluacion,z.fecha_pago  from empleado u inner join empleado_telefono_ditail d on u.id_empleado = d.id_empleado inner join telefono t on d.id_telefono = t.id_telefono inner join empleado_Direccion_Detail X on U.id_empleado = X.id_empleado inner join Direccion R on X.ID_Direccion = R.ID_Direccion inner join provincia P on R.ID_Provincia = P.ID_Provincia inner join canton C on R.ID_Canton = C.ID_Canton inner join Distrito I on R.ID_Distrito = I.ID_Distrito inner join empleado_correo_ditail y on u.id_empleado = y.id_empleado inner join  correo l on y.id_correo = l.id_correo inner join Rh z on u.id_empleado = z.id_rh inner join evaluacion e on z.id_evaluacion =  e.id_evaluacion ")
        datos = cur.fetchall()
        cur.close()    
        return datos

    def consulta_persona(self):
        cur = self.cnn.cursor()
        cur.execute(" select u.id_persona,u.cedula,u.nombre, u.primer_apellido, u.segundo_apellido, t.telefono,z.telefono, P.provincia, C.Canton, I.distrito,u.fecha_nacimiento,e.cedula, e.nombre,e.primer_apellido,e.segundo_apellido,e.parentesco,e.fecha_nacimiento from persona u inner join encargado e on  u.id_persona = e.id_persona inner join persona_telefono_ditail d on u.id_persona = d.id_persona inner join telefono t on  d.id_telefono = t.id_telefono inner join persona_encargado_telefono_ditail y on u.id_persona = y.id_persona inner join telefono z on  y.id_telefono = z.id_telefono inner join encargado_Direccion_Detail X on e.id_encargado = X.id_encargado inner join Direccion R on X.ID_Direccion = R.ID_Direccion inner join provincia P on R.ID_Provincia = P.ID_Provincia inner join canton C on R.ID_Canton = C.ID_Canton inner join Distrito I on R.ID_Distrito = I.ID_Distrito ")
        datos = cur.fetchall()
        cur.close()    
        return datos

    def consulta_proyecto_empleado(self):
        cur = self.cnn.cursor()
        cur.execute(" select e.id_empleado, e.nombre,e.primer_apellido,e.segundo_apellido, e.puesto, p.nombre, p.gasto,a.objetivo,v.monto from  empleado e inner join proyecto_empleado_ditail d on e.id_empleado= d.id_empleado inner join proyecto p on d.id_proyecto = p.id_proyecto inner join planificador_proyectos a on a.id_proyecto = p.id_proyecto inner join servicios v on p.id_proyecto = v.id_proyecto; ")
        datos = cur.fetchall()
        cur.close()    
        return datos

    def consulta_persona_voluntario(self):
        cur = self.cnn.cursor()
        cur.execute(" select e.id_voluntario, e.nombre,e.primer_apellido,e.segundo_apellido, p.nombre,a.objetivo,p.gasto from  voluntario e inner join proyecto_voluntario_ditail d on e.id_voluntario= d.id_voluntario inner join proyecto p on d.id_proyecto = p.id_proyecto inner join planificador_proyectos a on a.id_proyecto = p.id_proyecto;")
        datos = cur.fetchall()
        cur.close()    
        return datos

    def consulta_dep_admi(self):
        cur = self.cnn.cursor()
        cur.execute(" select * from dep_administrativo")
        datos = cur.fetchall()
        cur.close()    
        
        return datos

    def consulta_total_ingreso(self):
        cur = self.cnn.cursor()
        cur.execute(" select sum(monto) from subDep_finanzas")
        row = cur.fetchone()
        datos = row[0]
        cur.close()    
        
        return datos

    def consulta_total_fondo(self):
        cur = self.cnn.cursor()
        cur.execute("select sum(monto) from fondos")
        row = cur.fetchone()
        datos = row[0]
        cur.close()    
        
        return datos

    def consulta_total_gasto(self):
        cur = self.cnn.cursor()
        cur.execute("select sum(gastos) from gastos")
        row = cur.fetchone()
        datos = row[0]
        cur.close()    
        
        return datos

    def consulta_ingreso(self):
        cur = self.cnn.cursor()
        cur.execute(" select * from subDep_finanzas")
        datos = cur.fetchall()
        cur.close()    
        
        return datos

    def consulta_fondos(self):
        cur = self.cnn.cursor()
        cur.execute(" select * from fondos")
        datos = cur.fetchall()
        cur.close()    
        
        return datos

    def consulta_gastos(self):
        cur = self.cnn.cursor()
        cur.execute(" select * from gastos")
        datos = cur.fetchall()
        cur.close()    
        
        return datos
#Codigo para buscar un cliente especifico mandandole el id a la tabla usuario, el fetchone para conseguir un solo dato
    def buscar_cliente(self, id_usuario):
        cur = self.cnn.cursor()
        sql= "SELECT * FROM usuarios WHERE id_usuario = {}".format(id_usuario)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos
#optiene los datos de la clase pasada insertandolo en la tabla, el selec mas para optener el ultimo id insertado para direccion
    def inserta_cliente(self,nombre, primer_apellido, segundo_apellido, telefono, provincia, canton, distrito):
        cur = self.cnn.cursor()
        curs = self.cnn.cursor()
        cursor = self.cnn.cursor()
        cur1= self.cnn.cursor()

        curp = self.cnn.cursor()
        curc = self.cnn.cursor()
        curd = self.cnn.cursor()

        curx = self.cnn.cursor()
        curz = self.cnn.cursor()

       

        sql='''INSERT INTO empleado (nombre, primer_apellido, segundo_apellido) 
        VALUES('{}', '{}', '{}') '''.format(nombre, primer_apellido, segundo_apellido)
        
        id = ("SELECT MAX(id_usuario) from empleado ")
        cursor.execute(id)
        row = cursor.fetchone()
        id_p = row[0]
        cursor.close()

        sqlt='''INSERT INTO telefono (telefono) 
        VALUES('{}')'''.format(telefono)

        cur.execute(sql)
        curs.execute(sqlt)
        n=cur.rowcount
        m=curs.rowcount
        self.cnn.commit() 
        cur.close()
        curs.close()
        curs.close()

        id = ("SELECT MAX(id_usuario) from empleado ")
        cursor.execute(id)
        row = cursor.fetchone()
        id_p = row[0]
        cursor.close()
        
       

        sqlD='''INSERT INTO empleado_telefono_detail (id_empleado, id_telefono) 
        VALUES('{}', '{}')'''.format(id_p, id_p)      
        cur1.execute(sqlD)
        x=cur1.rowcount
        self.cnn.commit() 
        cur1.close()

        cursor.close()

        print(provincia)
        print(canton)

        idp = ("select ID_Provincia from Provincia where Provincia = '{}' ").format(str(provincia))
        curp.execute(idp)
        IP_Provincia = curp.fetchone()
        IP1 = IP_Provincia[0]
        print(IP1)
        
        idc = ("select ID_Canton from Canton where Canton = '{}' ").format(canton)
        curc.execute(idc)
        IP_Canton = curc.fetchone()
        IP2 = IP_Canton[0]
        print(IP2)

        sqli = ("select d.ID_Distrito from canton c inner join canton_distrito_detail I on C.ID_Canton = I.ID_Canton inner join distrito d on I.ID_Distrito = D.ID_Distrito Where c.ID_Canton = '{}' and d.Distrito = '{}' ").format(IP2,str(distrito))
        curd.execute(sqli)
        IP_Distrito = curd.fetchone()
        IP3 = IP_Distrito[0]
        print(IP3)

        sqlX='''insert into Direccion (ID_Direccion, ID_Provincia, ID_Canton, ID_Distrito)
        VALUES('{}', '{}', '{}', '{}')'''.format(id_p, IP1, IP2, IP3)      
        curx.execute(sqlX)
        self.cnn.commit()
        print("hola")

        curp.close()  
        curd.close()  
        curc.close()
        curx.close()

        print(id_p)
        ip_2 = id_p

        sqlz='''insert into Cliente_Direccion_Detail (id_empleado, ID_Direccion) 
        VALUES('{}', '{}')'''.format(id_p, ip_2) 
        
        curz.execute(sqlz)
        self.cnn.commit()
        
        curz.close()


        return n,m,x

# elimina el dato selecionado en el grid con un delete en tablas
    def elimina_cliente(self,id_usuario):
        cur = self.cnn.cursor()
        curs = self.cnn.cursor()
        curx = self.cnn.cursor()
        curz = self.cnn.cursor()

        print(id_usuario)
        cursor = self.cnn.cursor()
        sqld='''DELETE FROM empleado_telefono_detail WHERE id_telefono = {}'''.format(id_usuario)
        sqlx='''delete from empleado_Direccion_Detail WHERE ID_Direccion = {}'''.format(id_usuario)
        sqlz='''delete from direccion WHERE ID_Direccion = {}'''.format(id_usuario)


        sql='''DELETE FROM empleado WHERE id_empleado = {}'''.format(id_usuario)
        sqlt='''DELETE FROM telefono WHERE id_telefono = {}'''.format(id_usuario)
        
        
        cursor.execute(sqld)
        curx.execute(sqlx)
        curz.execute(sqlz)
        cur.execute(sql)
        curs.execute(sqlt)
        
        

        n=cur.rowcount
        m=curs.rowcount
        x=curs.rowcount
        
        self.cnn.commit()    
        cur.close()
        curs.close()
        curx.close()
        curz.close()
        cursor.close()
        return n,m,x

    def modifica_cliente(self,id_usuario,nombre, primer_apellido, segundo_apellido,telefono, provincia, canton, distrito):
        cur = self.cnn.cursor()
        curs = self.cnn.cursor()

        curp = self.cnn.cursor()
        curc = self.cnn.cursor()
        curd = self.cnn.cursor()

        curx = self.cnn.cursor()

        sql='''UPDATE empleado SET nombre='{}', primer_apellido='{}', segundo_apellido='{}'
         WHERE id_empleado={}'''.format(nombre, primer_apellido, segundo_apellido,id_usuario)
        sqlt='''UPDATE telefono SET  telefono='{}'
         WHERE id_telefono={}'''.format(telefono,id_usuario)
        cur.execute(sql)
        curs.execute(sqlt)
        n=cur.rowcount
        m=curs.rowcount
        self.cnn.commit()    
        cur.close()
        curs.close()    

        idp = ("select ID_Provincia from Provincia where Provincia = '{}' ").format(str(provincia))
        curp.execute(idp)
        IP_Provincia = curp.fetchone()
        IP1 = IP_Provincia[0]
        print(IP1)
        
        idc = ("select ID_Canton from Canton where Canton = '{}' ").format(canton)
        curc.execute(idc)
        IP_Canton = curc.fetchone()
        IP2 = IP_Canton[0]
        print(IP2)

        sqli = ("select d.ID_Distrito from canton c inner join canton_distrito_detail I on C.ID_Canton = I.ID_Canton inner join distrito d on I.ID_Distrito = D.ID_Distrito Where c.ID_Canton = '{}' and d.Distrito = '{}' ").format(IP2,str(distrito))
        curd.execute(sqli)
        IP_Distrito = curd.fetchone()
        IP3 = IP_Distrito[0]
        print(IP3)

        sqlX='''UPDATE Direccion SET ID_Provincia='{}', ID_Canton='{}', ID_Distrito='{}' WHERE ID_Direccion = '{}' '''.format(IP1, IP2, IP3, id_usuario)      
        curx.execute(sqlX)
        self.cnn.commit()
        print("hola")

        curp.close()  
        curd.close()  
        curc.close()
        curx.close()

        return n,m


