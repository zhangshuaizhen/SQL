#-*- coding:utf-8 –*
__author__ = 'zhangshuaizhen'
import sqlite3
#创建数据库
conn = sqlite3.connect('test1.db')
#创建游标
cursor = conn.cursor()
#创建表，新增数据
sql = 'create table user (id varchar(20) primary key, name varchar(20))'
cursor.execute(sql)
sql = 'insert into user (id, name) values (\'1\', \'Michael\')'
cursor.execute(sql)
#当前处理的行数
rs = cursor.rowcount
print rs
cursor.execute('select * from user where id=?', ('1',))
#查看所有数据
values = cursor.fetchall()
print values
#关闭游标、数据库
cursor.close()
conn.commit()
conn.close()