#coding=utf-8
import os
class DevelopmentConfig(object):
    MYSQL_HOST = 'localhost'                                                   
    MYSQL_PORT = '3306'                                                        
    MYSQL_USER = os.environ['LOGNAME']                                     
    MYSQL_PASS = ''                                                            
    MYSQL_DB = 'blog'                                                     
    SECRET_KEY = "12345"                                                       
    SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s?charset=utf8' %\
            (MYSQL_USER, MYSQL_PASS, MYSQL_HOST, MYSQL_PORT, MYSQL_DB)         
    DEBUG = False                                                              
    TESTING = False                                                            
