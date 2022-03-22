from dataclasses import dataclass
from genericpath import samefile
from random import sample
import sqlite3

con=sqlite3.connect("data.db",check_same_thread=False)

cur=con.cursor();

cur.execute("""create table if not exists student(id int,name varchar(20),department varchar(20))""");


def insertdetails(data):
    print(data)
    cur=con.cursor();
   # cur.execute(f'insert into student values("{data["id"]}","{data["name"]}","{data["department"]}")');
    


    if type(data)==list:
        cur.executemany(f'insert into student values(:id, :name, :department)', data);

    else:
        cur.execute(f'insert into student values("{data["id"]}" , "{data["name"]}" , "{data["department"]}")');
    con.commit();

def getdetail():
    cur=con.cursor();
    cur.execute("select * from student");
    data=cur.fetchall();
    con.commit();
    return(data);


def deleteStu(id):
    cur=con.cursor();
    cur.execute(f'delete from student where id={id}');
    con.commit();

def upd(data):
    cur=con.cursor();
    cur.execute(f'update student set name="{data["name"]}" where id={data["id"]}');
    con.commit();