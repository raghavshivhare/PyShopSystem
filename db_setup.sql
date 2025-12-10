create database pracdb;
use pracdb;
show tables in pracdb;


-- Creating tables
create table domain(user_id integer primary key not null,
user_name varchar(75) not null,
desig varchar(50) not null,
password char(64));
desc domain;

create table profiles(cust_id integer not null primary key,
name varchar(75) not null,
contact bigint not null,
gender varchar(10) not null,
email varchar(200),
add_l1 varchar(100),
add_l2 varchar(200),
add_l3 varchar(150),
city_state varchar(100) not null);
desc profiles;

create table products(prd_id integer not null primary key,
prd_name varchar(100) not null,
brand varchar(50) not null,
category varchar(50),
price integer,
quantity integer);
desc products;

create table sales(sale_id integer not null primary key,
prd_id integer not null,
cust_id integer,
sold_qu integer,
saledate datetime,
foreign key (prd_id) references products(prd_id)
on delete cascade on update cascade,
foreign key (cust_id) references profiles(cust_id)
on delete cascade on update cascade);
desc sales;

create table billdesk(inv_no integer primary key,
saledate datetime,
sale_id integer,
cust_id integer,
cust_name varchar(75),
prd_id integer,
prd_name varchar(100),
sold_qu integer,
price integer,
discount integer,
final_price integer,
foreign key (sale_id) references sales(sale_id)
on delete cascade on update cascade,
foreign key (cust_id) references profiles(cust_id)
on delete cascade on update cascade,
foreign key (prd_id) references products(prd_id)
on delete cascade on update cascade);
desc billdesk;


-- adding domain
insert into domain values(1, 'Administrator', 'admin', '1_eshop@domain');
select * from domain;


-- adding profiles
--add profiles here in profiles table


-- adding products
insert into products values(0002, 'Z Flip 5', 'Samsung', 'Mobile', 90000, '100');
insert into products values(0001, 'Z Fold 4', 'Samsung', 'Mobile', 150000, '100');
insert into products values(0003, 'S24 Ultra', 'Samsung', 'Mobile', 125000, '100');
insert into products values(0004, 'iPhone 15 Pro Max', 'Apple', 'Mobile', 144000, '100');
insert into products values(0005, '14 Ultra', 'Xiaomi', 'Mobile', 110000, '100');
insert into products values(0006, 'iPhone 15 Plus', 'Apple', 'Mobile', 80000, '100');
insert into products values(0007, 'V40 Pro', 'Vivo', 'Mobile', 50000, '100');
insert into products values(0008, 'Nord 4', 'Oneplus', 'Mobile', 30000, '100');
insert into products values(0009, 'Phone 2a', 'Nothing', 'Mobile', 25000, '100');
insert into products values(0010, '13 5G', 'Redmi', 'Mobile', 10000, '100');
insert into products values(0011, 'Smart TV 32','Samsung', 'Television', 20000, '75');
insert into products values(0012, 'Smart TV 5A 32', 'Xiaomi', 'Television', 15000, '75');
insert into products values(0013, 'TV Delite', 'Lloyd', 'Television', 8500, '25');
insert into products values(0014, 'Telefold 75', 'LG', 'Television', 350000, '20');
insert into products values(0015, 'OLED TV 65', 'Samsung', 'Television', 70000, '50');
insert into products values(0016, 'Laptop i3 12th Gen', 'HP', 'Computer', 40000, '100');
insert into products values(0017, 'Laptop Ryzen 5 7500', 'Lenovo', 'Computer', 55000, '100');
insert into products values(0018, 'Book 4 360 i7', 'Samsung', 'Computer', 75000, '100');
insert into products values(0019, 'ROG 15 Ryzen 9 8900', 'Asus', 'Computer', 94250, '50');
insert into products values(0020, 'Workstation 3 Desktop', 'Dell', 'Computer', 50000, '100');
select * from products;


-- adding sales
-- add sales here in the sales table


-- adding bills
-- add bills here in the billdesk table