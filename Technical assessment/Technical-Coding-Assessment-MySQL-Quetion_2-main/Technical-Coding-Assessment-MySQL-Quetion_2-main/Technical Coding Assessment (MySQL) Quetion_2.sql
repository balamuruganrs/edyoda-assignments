# Creating DataBase
create database Countries;

#view databases 
show databases;

#To select the database
use  Countries;

#view tables
show tables;

#Creating Table countries
create table countries(Country_ID int primary key,Country_Name varchar(25),Region_ID char(25));

# Inserting Values
insert into countries values(1,"Italy","ITA");
insert into countries values(2,"India","IND");
insert into countries values(3,"China","CHN");

#To view the table
select * from countries;


#Creating a duplicate table countries_new 

create table countries_new(COUNTRY_ID VARCHAR(2),COUNTRY_NAME varchar(40),REGION_ID DECIMAL(10,0));

#To view the table
select * from countries_new;

#To see the required output
desc countries_new;