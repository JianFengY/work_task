"""
Created on 2018/5/28
@Author: Jeff Yang
"""
import pymysql

conn = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='123456',
        db='pymysql',
        charset='utf8'
    )