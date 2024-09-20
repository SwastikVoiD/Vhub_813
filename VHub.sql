create database if not exists Vhub;
use Vhub;
create table if not exists user_master(
uname char(9) primary Key,
FName char(40),
LName char(40),
pwd char(20),
sex enum('M','F'),
hostel char(2),
room_no char(4),
phone char(10),
emergency char(10),
email char(50));
desc user_master;
alter table user_master add column access enum('S', 'W');
drop table user_master;