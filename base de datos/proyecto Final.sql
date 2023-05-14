create database Base_Datos;
use Base_Datos;

create table voluntario (
id_voluntario int not null auto_increment,
cedula varchar(64) not null unique,
nombre varchar(64) not null,
primer_apellido varchar(64) not null,
segundo_apellido varchar(64) not null,
fecha_nacimiento date not null,
primary key (id_voluntario,cedula)
);

create table empleado (
id_empleado int not null auto_increment,
cedula varchar(64) not null unique,
nombre varchar(64) not null,
primer_apellido varchar(64) not null,
segundo_apellido varchar(64) not null,
fecha_nacimiento date not null,
puesto varchar(64) not null,
primary key (id_empleado,cedula)
);

  

create table persona (
id_persona int not null auto_increment,
cedula varchar(64) not null unique,
nombre varchar(64) not null,
primer_apellido varchar(64) not null,
segundo_apellido varchar(64) not null,
fecha_nacimiento date not null,
primary key (id_persona,cedula)
);

create table encargado (
id_encargado int not null auto_increment,
cedula varchar(64) not null unique,
nombre varchar(64) not null,
primer_apellido varchar(64) not null,
segundo_apellido varchar(64) not null,
parentesco varchar(64) not null,
fecha_nacimiento date not null,
id_persona int unique,
constraint fk_persona_encargado foreign key (id_persona) references persona(id_persona),
primary key (id_encargado,cedula)
);
    
    
    
create table telefono (
id_telefono int not null auto_increment,
telefono varchar (60) not null,
primary key (id_telefono)
);

    
create table correo (
id_correo int not null auto_increment,
correo varchar (60) not null,
primary key (id_correo)
);


create table donador_anonimo(
id_donador_anonimo int not null auto_increment,
donacion int not null,
primary key (id_donador_anonimo)
);


create table organizacion_donante (
id_organizacion_donante int not null auto_increment,
nombre varchar (60) not null,
donacion int not null,
primary key (id_organizacion_donante)
);



create table proyecto(
id_proyecto int not null auto_increment,
nombre varchar (80) not null,
gasto int not null,
primary key (id_proyecto)
);

    

    
create table departamento(
id_departamento int not null auto_increment,
nombre varchar (60) not null,
id_empleado int,
constraint fk_empleado foreign key (id_empleado) references empleado(id_empleado),
primary key (id_departamento)
);

    
    
create table dep_administrativo(
id_dep_administrativo int not null auto_increment,
nombre_articulo varchar (60) not null,
cantidad int not null,
fecha_ingreso date  not null,
fecha_caducidad date  not null,
estado varchar (30) not null,
detalle varchar (60) not null,
precio int ,
primary key (id_dep_administrativo)
);

    
create table dep_mercadeo(
id_dep_mercadeo int not null auto_increment,
id_organizacion_donante int not null unique,
numero_contrato varchar (60) not null,
foreign key (id_organizacion_donante) references organizacion_donante(id_organizacion_donante),
primary key (id_dep_mercadeo)
);



create table servicios (
id_servicios int not null auto_increment,
servicio varchar (60) not null,
monto int not null,
id_proyecto int,
primary key (id_servicios)
);


    
create table evaluacion(
id_evaluacion int not null auto_increment,
evaluacion varchar (20) not null,
primary key (id_evaluacion)
);


    
create table Rh(
id_rh int not null auto_increment,
id_empleado int not null unique,
horas int not null,
salario int not null,
id_evaluacion int not null ,
fecha_pago date,
constraint FK_empleado_rh foreign key (id_empleado) references empleado(id_empleado),
constraint fk_evaluacion foreign key (id_evaluacion) references evaluacion(id_evaluacion),
primary key (id_rh)
);






create table planificador_proyectos(
id_planificador int not null auto_increment,
id_empleado int not null,
objetivo varchar (100) not null,
id_proyecto int not null,
foreign key (id_empleado) references empleado(id_empleado),
foreign key (id_proyecto) references proyecto(id_proyecto),
primary key (id_planificador)
);




create table junta_directiva (
id_junta_directiva int not null auto_increment,
id_empleado int not null unique,
cargo varchar (60) not null,
primary key (id_junta_directiva),
foreign key (id_empleado) references empleado(id_empleado)
);



create table subDep_finanzas (
subDep_finanzas int not null auto_increment,
monto int not null,
tipo varchar (60),
primary key (subDep_finanzas)

);




create table gastos(
id_gastos int not null auto_increment,
nombre varchar (60) ,
gastos int not null,
primary key (id_gastos)
);




create table fondos (
ID_fondos int not null auto_increment,
monto int not null,
tipo varchar (60) ,
primary key (ID_fondos)

);
INSERT INTO fondos( monto, tipo )
SELECT monto, tipo FROM subDep_finanzas;

INSERT INTO fondos( monto, tipo )
SELECT gastos, nombre FROM gastos;


create table dep_contabilidad (
id_dep_contabilidad int not null auto_increment,
mes VARCHAR(30) ,
ingresos_por_mes int,
gastos_por_mes int,
fondos_por_mes int,
primary key (id_dep_contabilidad)
);


CREATE TABLE provincia (
   	`ID_Provincia` INT,
    `Provincia` VARCHAR(30) unique,
	primary key(ID_Provincia)
);
CREATE TABLE canton (
	`ID_Canton` INT,
    `canton` VARCHAR(30) unique,
	primary key(ID_Canton)
	
);
CREATE TABLE distrito (
    	
   	`Id_Distrito` INT,
   	`distrito` VARCHAR(30),
	primary key(Id_Distrito)
	
);


create table empleado_telefono_ditail(
id_empleado int not null ,
id_telefono int not null ,
constraint pk_empleado_telefono primary key (id_empleado,id_telefono),
constraint fk_empleado_telefono foreign key (id_empleado) references empleado(id_empleado),
constraint  fk_telefono_empleado foreign key (id_telefono) references telefono(id_telefono)
);



create table empleado_correo_ditail(
id_empleado int not null ,
id_correo int not null unique,
constraint pk_empleado_correo primary key (id_empleado,id_correo),
constraint fk_empleado_correo foreign key (id_empleado) references empleado(id_empleado),
constraint  fk_correo_empleado foreign key (id_correo) references correo(id_correo)
);



create table voluntario_telefono_ditail(
id_voluntario int not null ,
id_telefono int not null ,
constraint pk_voluntario_telefono primary key (id_voluntario,id_telefono),
constraint fk_voluntario_telefono foreign key (id_voluntario) references voluntario(id_voluntario),
constraint  fk_telefono_voluntario foreign key (id_telefono) references telefono(id_telefono)
);


create table voluntario_correo_ditail(
id_voluntario int not null ,
id_correo int not null unique,
constraint pk_voluntario_correo primary key (id_voluntario,id_correo),
constraint fk_voluntario_correo foreign key (id_voluntario) references voluntario(id_voluntario),
constraint  fk_correo_voluntario foreign key (id_correo) references correo(id_correo)
);


create table persona_telefono_ditail(
id_persona int not null ,
id_telefono int not null ,
constraint pk_persona_telefono primary key (id_persona,id_telefono),
constraint fk_persona_telefono foreign key (id_persona) references persona(id_persona),
constraint  fk_telefono_persona foreign key (id_telefono) references telefono(id_telefono)
);

create table persona_encargado_telefono_ditail(
id_persona int not null ,
id_encargado int not null ,
id_telefono int not null ,
constraint pk_persona_encargado_telefono primary key (id_persona,id_telefono,id_encargado),
constraint fk_persona_encargado_telefono foreign key (id_persona) references persona(id_persona),
constraint  fk_telefono_persona_encargado foreign key (id_telefono) references telefono(id_telefono),
constraint fk_persona_encargado_telefonos foreign key (id_encargado) references encargado(id_encargado)
);

create table encargado_telefono_ditail(
id_encargado int not null ,
id_telefono int not null ,
constraint pk_encargado_telefono primary key (id_encargado,id_telefono),
constraint fk_encargado_telefono foreign key (id_encargado) references encargado(id_encargado),
constraint  fk_telefono_encargado foreign key (id_telefono) references telefono(id_telefono)
);


create table encargado_correo_ditail(
id_encargado int not null ,
id_correo int not null unique,
constraint pk_encargado_correo primary key (id_encargado,id_correo),
constraint fk_encargado_correo foreign key (id_encargado) references encargado(id_encargado),
constraint  fk_correo_encargado foreign key (id_correo) references correo(id_correo)
);



create table Organizacion_telefono_ditail(
id_organizacion_donante int not null ,
id_telefono int not null ,
constraint pk_Organizacion_telefono primary key (id_organizacion_donante,id_telefono),
constraint fk_Organizacion_telefono foreign key (id_organizacion_donante) references organizacion_donante(id_organizacion_donante),
constraint  fk_telefono_Organizacion foreign key (id_telefono) references telefono(id_telefono)
);


create table Organizacion_correo_ditail(
id_organizacion_donante int not null ,
id_correo int not null unique,
constraint pk_Organizacion_correo primary key (id_organizacion_donante,id_correo),
constraint fk_Organizacion_correo foreign key (id_organizacion_donante) references organizacion_donante(id_organizacion_donante),
constraint  fk_correo_Organizacion foreign key (id_correo) references correo(id_correo)
);


create table proyecto_empleado_ditail(
id_proyecto int not null ,
id_empleado int not null ,
constraint pk_proyecto_empleado primary key (id_proyecto,id_empleado),
constraint fk_proyecto_empleado foreign key (id_proyecto) references proyecto(id_proyecto),
constraint  fk_empleado_proyecto foreign key (id_empleado) references empleado(id_empleado)
);



create table proyecto_voluntario_ditail(
id_proyecto int not null ,
id_voluntario int not null ,
constraint pk_proyecto_voluntario primary key (id_proyecto,id_voluntario),
constraint fk_proyecto_voluntario foreign key (id_proyecto) references proyecto(id_proyecto),
constraint  fk_voluntario_proyecto foreign key (id_voluntario) references voluntario(id_voluntario)
);


CREATE TABLE Provincia_Canton_Detail (
    `ID_Provincia` INT,
   `ID_canton` INT unique,
	foreign key (ID_Provincia) references provincia (ID_Provincia),
	foreign key (ID_Canton) references canton (ID_Canton),
	primary key(ID_Provincia,ID_canton)	
);
CREATE TABLE Canton_Distrito_Detail (
    `ID_canton` INT,
    `id_distrito` INT,
	foreign key (Id_Distrito) references distrito(Id_Distrito),
	foreign key (ID_Canton) references canton (ID_Canton),
	primary key(Id_Distrito,ID_Canton)	
);
create table Direccion(
ID_Direccion int not null ,
ID_Provincia int not null,
ID_Canton int  not null,
ID_Distrito int not null,
constraint PK_Provincia_Canton_Distrito primary key (ID_Direccion,ID_Provincia,ID_Canton,ID_Distrito),
constraint FK_Provincias foreign key (ID_Provincia) references Provincia(ID_Provincia),
constraint FK_Cantones foreign key (ID_Canton)references Canton(ID_Canton),
constraint FK_Distritos foreign key (ID_Distrito)references Distrito(ID_Distrito) 
);

create table empleado_Direccion_Detail(
id_empleado int not null unique,
ID_Direccion int not null,
constraint PK_empleado_Direccion primary key (id_empleado,ID_Direccion),
constraint FK_empleado_Direccion foreign key (id_empleado ) references empleado(id_empleado),
constraint FK_Direccion_empleado foreign key (ID_Direccion)references Direccion(ID_Direccion) 
);
create table voluntario_Direccion_Detail(
id_voluntario int not null unique,
ID_Direccion int not null,
constraint PK_voluntario_Direccion primary key (id_voluntario,ID_Direccion),
constraint FK_voluntario_Direccion foreign key (id_voluntario ) references voluntario(id_voluntario),
constraint FK_Direccion_voluntario foreign key (ID_Direccion)references Direccion(ID_Direccion) 
);
create table encargado_Direccion_Detail(
id_encargado int not null unique,
ID_Direccion int not null,
constraint PK_encargado_Direccion primary key (id_encargado,ID_Direccion),
constraint FK_encargado_Direccion foreign key (id_encargado ) references encargado(id_encargado),
constraint FK_Direccion_encargado foreign key (ID_Direccion)references Direccion(ID_Direccion) 
);








