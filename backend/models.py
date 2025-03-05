"""
O módulo model.py define os modelos SQLAlchemy de forma agnóstica ao banco de dados.
Os modelos são as classes que definem as tabelas do banco de dados.
Objetivo: Definir nomes, colunas e tipos de dados das tabelas.
Campos gerados automaticamente:
    - id: Tipo Integer com parâmetro primary_key=True, 
    - created_at: Tipo DateTime com parâmetro default=func.now()
"""
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base


class BookModel(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    isbn = Column(String, index=True)
    publisher = Column(String, index=True)
    genre = Column(String, index=True)
    page_count = Column(Integer, index=True)
    language = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float, index=True)
    created_at = Column(DateTime(timezone=True), default=func.now(), index=True)
