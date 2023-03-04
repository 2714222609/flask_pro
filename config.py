# encoding: utf-8
import os

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'zhiliaooa_course'
USERNAME = 'root'
PASSWORD = '111111'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = True

DEBUG = True

SECRET_KEY = os.urandom(24)
