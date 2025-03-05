"""
O módulo router.py define as rotas da API utilizando o FastAPI.
Objetivos:
    - Definir as rotas.
    - Definir quais funções que serão executadas em cada rota.
Parâmetros das funções:
    - path: Caminho da rota.
    - methods: Métodos HTTP que a rota aceita.
    - response_model: Schema que é retornado pela rota.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import BookResponse, BookUpdate, BookCreate
from typing import List
from crud import (
    create_book,
    get_book,
    get_books,
    delete_book,
    update_book,
)

router = APIRouter()


@router.post("/books/", response_model=BookResponse)
def create_book_route(book: BookCreate, db: Session = Depends(get_db)):
    """
    Rota para criar livros.
    """
    return create_book(db=db, book=book)


@router.get("/books/", response_model=List[BookResponse])
def read_all_books_route(db: Session = Depends(get_db)):
    """
    Rota para buscar todos os livros.
    """
    books = get_books(db)
    return books


@router.get("/books/{book_id}", response_model=BookResponse)
def read_book_route(book_id: int, db: Session = Depends(get_db)):
    """
    Rota para buscar um livro a partir do id fornecido.
    """
    db_book = get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@router.delete("/books/{book_id}", response_model=BookResponse)
def delete_book_route(book_id: int, db: Session = Depends(get_db)):
    """
    Rota para excluir produtos.
    """
    db_book = delete_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@router.put("/books/{book_id}", response_model=BookResponse)
def update_book_route(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    """
    Rota para atualizar produtos.
    """
    db_book = update_book(db, book_id=book_id, book=book)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book
