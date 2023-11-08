class BaseConfig():
    """Configuración de tipo Base en la cual se ponen los siguientes parametros::
    
        | 1.- Secret key
        | 2.- Debug
        | 3.- Testing
        | 4.- SqlAlchemy Database URI
        | 5.- SqlAlchemy Track Modifications
    """
    SECRET_KEY = 'Key'
    TESTING = False
    #postgres://vdaqggkxvnuqbc:0f26d7e636bf61ff65a34d744ec88c09d4174cf6e46398ba4d2f2dddd1daa708@ec2-54-157-79-121.compute-1.amazonaws.com:5432/d33jlarmgmial0
    SQLALCHEMY_DATABASE_URI = "postgresql://vdaqggkxvnuqbc:0f26d7e636bf61ff65a34d744ec88c09d4174cf6e46398ba4d2f2dddd1daa708@ec2-54-157-79-121.compute-1.amazonaws.com:5432/d33jlarmgmial0"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(BaseConfig):
    """Configuración de producción
    
    Parameters
    -----------
    BaseConfig : class
        Configuración base
    """
    DEBUG = False
    
class DevelopmentConfig(BaseConfig):
    """Configuración de Desarrollo
    
    Parameters
    -----------
    BaseConfig : class
        Configuración base
    """
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'Desarrollo key'