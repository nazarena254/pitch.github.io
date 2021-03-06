import os

class Config:  
    #General configuration parent class
    # SQLALCHEMY_DATABASE_URI= os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://nancyngunjiri1:nazarena123@localhost:5432/pitch'
    SECRET_KEY= os.environ.get('SECRET_KEY')

    # email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME= os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD= os.environ.get('MAIL_PASSWORD')
    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI= os.environ.get('DATABASE_URL')
    
class ProdConfig(Config):  # this configuration is needed during heroku deployment
    SQLALCHEMY_DATABASE_URI= 'postgresql://hecytzbkhcqioo:e648b842d38703a7a293262c2155b4391c11f02adabdbaeec28c48d8c75f1329@ec2-54-172-175-251.compute-1.amazonaws.com:5432/d7npve7pb3k8op'
    
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://nancyngunjiri1:nazarena123@localhost:5432/pitch'
    # SQLALCHEMY_DATABASE_URI= os.environ.get('DATABASE_URL')
    DEBUG = True
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}