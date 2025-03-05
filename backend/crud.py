"""
O módulo crud.py define as funções de CRUD utilizando o SQLAlchemy ORM.
"""
from sqlalchemy.orm import Session
from schemas import BookUpdate, BookCreate
from models import BookModel


def get_book(db: Session, book_id: int):
    """
    Função que retorna um livro a partir do id fornecido.
    """
    return db.query(BookModel).filter(BookModel.id == book_id).first()


def get_books(db: Session):
    """
    Função que retorna todos os livros.
    """
    return db.query(BookModel).all()


def create_book(db: Session, book: BookCreate):
    """
    Função para criar livros.
    Recebe uma instância da classe criada no Pydantic e converte para o ORM.
    """
    db_book = BookModel(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int):
    """
    Função para excluir livros.
    """
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()
    db.delete(db_book)
    db.commit()
    return db_book


def update_book(db: Session, book_id: int, book: BookUpdate):
    """
    Função para atualizar livros.
    """
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()

    if db_book is None:
        return None

    if book.title is not None:
        db_book.title = book.title
    if book.author is not None:
        db_book.author = book.author
    if book.isbn is not None:
        db_book.isbn = book.isbn
    if book.publisher is not None:
        db_book.publisher = book.publisher
    if book.genre is not None:
        db_book.genre = book.genre
    if book.page_count is not None:
        db_book.page_count = book.page_count
    if book.language is not None:
        db_book.language = book.language
    if book.description is not None:
        db_book.description = book.description
    if book.price is not None:
        db_book.price = book.price

    db.commit()
    return db_book
