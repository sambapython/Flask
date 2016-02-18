create table if not exists company(id SERIAL primary key, name varchar(50), address text);
create table if not exists  timings(id SERIAL primary key, name varchar(50),from1 date, to1 date);
create table if not exists  course(id SERIAL primary key, name varchar(50), duration int, fee float);
create table if not exists  client(id SERIAL primary key, name varchar(50), address text, cell varchar(20),course_id int references course(id),remark1 text,remark2 text,remark3 text,remark4 text);
