#-*- coding:utf-8 –*
__author__ = 'zhangshuaizhen'
import mysql.connector
#连接到mysql数据库
conn = mysql.connector.connect(user='root', password='zhang123', database='test1', use_unicode=True)
#创建游标
cursor = conn.cursor()
#新增数据
cursor.execute('insert into user (id, name) values (%s, %s)', ['2', 'Michael'])
#当前处理的数据行数
rs=cursor.rowcount
print rs
#提交、执行
conn.commit()
cursor.execute('select * from user where id = %s', ('2',))
values = cursor.fetchall()
print values
#关闭游标、数据库
cursor.close()
conn.close()