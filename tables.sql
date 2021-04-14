
create table Login ( username varchar(20) primary key ,password varchar(20));
insert into Login values('S20190046','Tusharsai');
insert into Login values('A20191234','Bigchungus');

create table employees(EID varchar(20) primary key , Name varchar(30) , Gender varchar(10) , contact bigint , email varchar(60));
drop table employees;
drop table students;
drop table books;
use db;
create table students( SID varchar(20) primary key , Name varchar(30) , Gender varchar(10) , contact bigint , email varchar(60) , moneydue int);

create table books(bid  int primary key, title varchar(30), author varchar(16), copies int, remarks varchar(35), publisher varchar(25));
create table borrow (sid varchar(20) not null , bid int not null , issuedate date not null , duedate date generated always as ((issuedate + interval 14 day)) virtual);
alter table borrow
add constraint pk_borrow primary key (sid , bid , issuedate);
alter table borrow 
add CONSTRAINT borrow_sid_fk foreign key (sid)  references students(sid);
alter table borrow
add CONSTRAINT borrow_bid_fk foreign key (bid) references books (bid); 
create table returnbook(sid int not null , bid int not null , issuedate date not null , duedate date generated always as ((issuedate + interval 14 day)) virtual , moneydue int , returndate date );

alter table returnbook
add constraint pk_return primary key (sid , bid , returndate);
alter table borrow 
add CONSTRAINT returnbook_sid_fk foreign key (sid)  references students(sid);
alter table borrow
add CONSTRAINT returnbook_bid_fk foreign key (bid) references books (bid); 
use db;
drop table borrow;
drop table returnbook;
insert into Login values('E20192130','12345678');


insert into books values(101 , 'The Book' , 'Hello' , 3 , '' , '1234');
create table borrow (sid varchar(20) not null , bid int not null , issuedate date not null , duedate date generated always as ((issuedate + interval 14 day)) virtual);
alter table borrow
add constraint pk_borrow primary key (sid , bid , issuedate);
alter table borrow 
add CONSTRAINT borrow_sid_fk foreign key (sid)  references students(sid);
alter table borrow
add CONSTRAINT borrow_bid_fk foreign key (bid) references books (bid); 
create table returnbook(sid int not null , bid int not null , issuedate date not null , duedate date generated always as ((issuedate + interval 14 day)) virtual , moneydue int , returndate date );
alter table returnbook
add constraint pk_return primary key (sid , bid , returndate);
alter table borrow 
add CONSTRAINT returnbook_sid_fk foreign key (sid)  references students(sid);
alter table borrow
add CONSTRAINT returnbook_bid_fk foreign key (bid) references books (bid); 
select * from students;
drop table students;
create table students( SID varchar(20) primary key , Name varchar(30) , Gender varchar(10) , age int , contact bigint , email varchar(60) , moneydue int);
insert into students values('S20190046' , 'Sai Tushar' , 'Male' , 20 , 9867739628 , 'saitusharb0901@gmail.com' , 0);
use db;
drop table employees;
create table employees(EID varchar(20) primary key , Name varchar(30) , Gender varchar(10)  , age int, contact bigint , email varchar(60));
insert into employees values('E20192130' , 'Rahul' , 'Male' , 45 , 9967053597,'tushargod7@gmail.com');