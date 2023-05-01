# SocioAI
import pymysql as p


global cur,con

def connectdb():
    global con,cur
    #Enter your username and password of MySQL
    con=p.connect(host="localhost",user="root",passwd="database")
    cur=con.cursor()
    cur.execute('CREATE DATABASE IF NOT EXISTS SocioAI')
    cur.execute('USE SocioAI')
    global enter
    if enter==1:
        l='CREATE TABLE IF NOT EXISTS NormalUser(u_id int(10),name varchar(30),password varchar(20),ph_no int(10),fav_query_pointer int(10))'
        k='CREATE TABLE IF NOT EXISTS ProUser(u_id int(10),name varchar(30),password varchar(20),ph_no int(10),fav_query_pointer int(10),alter_query varchar(20),alter_solution varchar(20))'
        m='CREATE TABLE IF NOT EXISTS Adminpermit(u_id int(10),name varchar(30),password varchar(20),ph_no int(10),fav_query_pointer int(10),alter_query varchar(20),alter_solution varchar(20))'
        n='CREATE TABLE IF NOT EXISTS AddQuery(id int(2) NOT NULL AUTO_INCREMENT, alter_query varchar(100),alter_solution varchar(50), PRIMARY KEY (id))'
        b='CREATE TABLE IF NOT EXISTS QueryHospital(disease varchar(50),medicine varchar(50), query_pointer int(3))'
        j='CREATE TABLE IF NOT EXISTS QueryEducation(name varchar(50), avg_package int(10), nirf_ranking int(3), criteria varchar(40), query_pointer int(3))'
        cur.execute(l)
        cur.execute(k)
        cur.execute(m)
        cur.execute(n)
        cur.execute(b)
        cur.execute(j)
        enter=enter+1
    query='SELECT * FROM NormalUser'
    cur.execute(query)

def closedb():
    global con,cur
    cur.close()
    con.close()

enter=1
