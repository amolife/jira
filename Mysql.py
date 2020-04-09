#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 21:22:52 2020

@author: forward_ubuntu
"""
import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "phpmyadmin", "forward", "Fuckworld", charset='utf8')
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()
print("Database version : %s " % data)

# SQL 插入语句
sql = """INSERT INTO PlayMYSQL(id,title,name,date)
         VALUES (5,'仙女', '嫦娥', '2020/04/08')"""
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()



sql = "SELECT * FROM PlayMYSQL"
try:
   cursor.execute(sql)
except:
   # Rollback in case there is any error
   db.rollback()
results = cursor.fetchall()

for re in results:
    print(re)

# 关闭数据库连接
db.close()

