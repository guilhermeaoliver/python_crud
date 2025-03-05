"""
O módulo database.py faz a configuração do banco de dados utilizando SQLAlchemy.
Objetivos:
    - Criar a conexão com o banco de dados.
    - Criar a sessão do banco de dados.
Para mudar o banco de dados: Alterar a URL de conexão (variável SQLALCHEMY_DATABASE_URL)
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgres/mydatabase"

# Cria o motor, que se conecta com o banco de dados
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Cria a sessão, que executa as queries no banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos declarativos (ORM)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
