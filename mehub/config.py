import os
class DevelopmentConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://ubuntu:thinkful@localhost:5432/mehub"
    DEBUG = True
    SECRET_KEY = "fredtestkey"