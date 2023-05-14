create database loginpass;
use loginpass;
create table login_datos (
id_login int not null auto_increment,
Users varchar (20) not null,
Password varchar (20) not null,
primary key (id_login));

insert into login_datos (Users, Password)
values
('poke', '1896'),
('1', '2');

