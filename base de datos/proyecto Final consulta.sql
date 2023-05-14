use Base_Datos;

select u.id_empleado,u.cedula,u.nombre, u.primer_apellido, u.segundo_apellido, t.telefono, P.provincia, C.Canton, I.distrito,l.correo,u.fecha_nacimiento,z.horas,z.salario,e.evaluacion,z.fecha_pago  
from empleado u 
inner join empleado_telefono_ditail d 
on u.id_empleado = d.id_empleado 
inner join telefono t 
on d.id_telefono = t.id_telefono 
inner join empleado_Direccion_Detail X 
on U.id_empleado = X.id_empleado 
inner join Direccion R 
on X.ID_Direccion = R.ID_Direccion 
inner join provincia P 
on R.ID_Provincia = P.ID_Provincia 
inner join canton C 
on R.ID_Canton = C.ID_Canton 
inner join Distrito I 
on R.ID_Distrito = I.ID_Distrito 
inner join empleado_correo_ditail y 
on u.id_empleado = y.id_empleado 
inner join  correo l 
on y.id_correo = l.id_correo 
inner join Rh z 
on u.id_empleado = z.id_rh 
inner join evaluacion e 
on z.id_evaluacion =  e.id_evaluacion;

select u.id_persona,u.cedula,u.nombre, u.primer_apellido, u.segundo_apellido, t.telefono,z.telefono, P.provincia, C.Canton, I.distrito,u.fecha_nacimiento,e.cedula, e.nombre,e.primer_apellido,e.segundo_apellido,e.parentesco,e.fecha_nacimiento 
from persona u 
inner join encargado e 
on  u.id_persona = e.id_persona 
inner join persona_telefono_ditail d  
on u.id_persona = d.id_persona 
inner join telefono t 
on  d.id_telefono = t.id_telefono 
inner join persona_encargado_telefono_ditail y 
on u.id_persona = y.id_persona 
inner join telefono z 
on  y.id_telefono = z.id_telefono 
inner join encargado_Direccion_Detail X 
on e.id_encargado = X.id_encargado 
inner join Direccion R  
on X.ID_Direccion = R.ID_Direccion  
inner join provincia P 
on R.ID_Provincia = P.ID_Provincia 
inner join canton C 
on R.ID_Canton = C.ID_Canton 
inner join Distrito I 
on R.ID_Distrito = I.ID_Distrito;

select e.id_empleado, e.nombre,e.primer_apellido,e.segundo_apellido, e.puesto, c.cargo
from  empleado e 
inner join junta_directiva c
on e.id_empleado = c.id_empleado;



select e.id_empleado, e.nombre,e.primer_apellido,e.segundo_apellido, e.puesto, p.nombre, p.gasto,a.objetivo,v.monto 
from  empleado e 
inner join proyecto_empleado_ditail d 
on e.id_empleado= d.id_empleado 
inner join proyecto p 
on d.id_proyecto = p.id_proyecto 
inner join planificador_proyectos a 
on a.id_proyecto = p.id_proyecto 
inner join servicios v 
on p.id_proyecto = v.id_proyecto; 


select e.id_voluntario, e.nombre,e.primer_apellido,e.segundo_apellido, p.nombre,a.objetivo,p.gasto
from  voluntario e
inner join proyecto_voluntario_ditail d
on e.id_voluntario= d.id_voluntario
inner join proyecto p
on d.id_proyecto = p.id_proyecto
inner join planificador_proyectos a
on a.id_proyecto = p.id_proyecto;

select u.id_empleado,u.cedula,u.nombre, u.primer_apellido, u.segundo_apellido,d.nombre
from empleado u 
inner join departamento d
on u.id_empleado = d.id_empleado;



select * from servicios;
select * from planificador_proyectos;
select * from servicios;


select sum(monto) from subDep_finanzas;
select sum(monto) from fondos;
select sum(gastos) from gastos;

CREATE VIEW view_trabajador
AS
select u.id_empleado,u.cedula,u.nombre, u.primer_apellido, u.segundo_apellido, t.telefono, P.provincia, C.Canton, I.distrito,l.correo,u.fecha_nacimiento,z.horas,z.salario,e.evaluacion,z.fecha_pago  
from empleado u 
inner join empleado_telefono_ditail d 
on u.id_empleado = d.id_empleado 
inner join telefono t 
on d.id_telefono = t.id_telefono 
inner join empleado_Direccion_Detail X 
on U.id_empleado = X.id_empleado 
inner join Direccion R 
on X.ID_Direccion = R.ID_Direccion 
inner join provincia P 
on R.ID_Provincia = P.ID_Provincia 
inner join canton C 
on R.ID_Canton = C.ID_Canton 
inner join Distrito I 
on R.ID_Distrito = I.ID_Distrito 
inner join empleado_correo_ditail y 
on u.id_empleado = y.id_empleado 
inner join  correo l 
on y.id_correo = l.id_correo 
inner join Rh z 
on u.id_empleado = z.id_rh 
inner join evaluacion e 
on z.id_evaluacion =  e.id_evaluacion;

select * from view_trabajador;

