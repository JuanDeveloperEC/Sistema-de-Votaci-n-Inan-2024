from sqlalchemy import Boolean, Column,Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



DATABASE_URL = "mysql+mysqlconnector://root:666666@localhost/sistema_votaciones"


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush =False, bind=engine)

Base = declarative_base()

def getbd ():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()    

class Usuarios(Base):
    __tablename__ = "usuarios"
    idusuarios = Column (Integer, primary_key= True,index=True)
    nombre = Column(String(50))
    apellido = Column(String(50))
    cedula = Column(String(20), unique=True, index=True)
    carrera  = Column(String (50))
    ciclo  = Column(String (50))
    estado = Column(Boolean)

class Votaciones(Base):
   __tablename__ = "votaciones"
   idvotaciones = Column (Integer, primary_key= True,index=True)
   voto = Column (Integer)
   




