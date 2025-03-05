"""
O módulo schemas.py define os schemas do Pydantic, que são as classes com as definições dos tipos de dados.
Objetivos:
    - Validar os dados que são recebidos na API
    - Definir os tipos de dados que são retornados pela API.
"""
from pydantic import BaseModel, PositiveFloat, PositiveInt, field_validator
from pydantic_extra_types.isbn import ISBN
from enum import Enum
from datetime import datetime
from typing import Optional


class GenreBase(Enum):
    genre_1 = "Adventure"
    genre_2 = "Biography"
    genre_3 = "Children's"
    genre_4 = "Classics"
    genre_5 = "Crime"
    genre_6 = "Drama"
    genre_7 = "Dystopian"
    genre_8 = "Fantasy"
    genre_9 = "Fiction"
    genre_10 = "Graphic Novels"
    genre_11 = "Historical Fiction"
    genre_12 = "Horror"
    genre_13 = "Humor"
    genre_14 = "Memoir"
    genre_15 = "Mystery"
    genre_16 = "Non-fiction"
    genre_17 = "Poetry"
    genre_18 = "Romance"
    genre_19 = "Science Fiction"
    genre_20 = "Self-Help"
    genre_21 = "Spirituality"
    genre_22 = "Thriller"
    genre_23 = "Travel"
    genre_24 = "Western"
    genre_25 = "Young Adult"
    genre_26 = "Other"


class LanguageBase(Enum):
    language_1 = "Arabic"
    language_2 = "Bengali"
    language_3 = "Egyptian Arabic"
    language_4 = "English"
    language_5 = "French"
    language_6 = "German"
    language_7 = "Hausa"
    language_8 = "Hindi"
    language_9 = "Italian"
    language_10 = "Japanese"
    language_11 = "Javanese"
    language_12 = "Korean"
    language_13 = "Mandarin Chinese"
    language_14 = "Marathi"
    language_15 = "Portuguese"
    language_16 = "Russian"
    language_17 = "Spanish"
    language_18 = "Tamil"
    language_19 = "Telugu"
    language_20 = "Turkish"
    language_21 = "Urdu"
    language_22 = "Vietnamese"
    language_23 = "Western Punjabi"
    language_24 = "Wu Chinese"
    language_25 = "Yue Chinese (Cantonese)"
    language_26 = "Other"


class BookBase(BaseModel):
    title: str
    author: str
    isbn: ISBN
    publisher: str
    genre: str
    page_count: PositiveInt
    language: str
    description: Optional[str] = None
    price: PositiveFloat

    @field_validator("genre")
    def check_categoria(cls, v):
        if v in [item.value for item in GenreBase]:
            return v
        raise ValueError("Invalid genre")

    @field_validator("language")
    def check_categoria(cls, v):
        if v in [item.value for item in LanguageBase]:
            return v
        raise ValueError("Invalid language")


class BookCreate(BookBase):
    pass


class BookResponse(BookBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    isbn: Optional[ISBN] = None
    publisher: Optional[str] = None
    genre: Optional[str] = None
    page_count: Optional[PositiveInt] = None
    language: Optional[str] = None
    description: Optional[str] = None
    price: Optional[PositiveFloat] = None

    @field_validator("genre")
    def check_categoria(cls, v):
        if v is None:
            return v
        if v in [item.value for item in GenreBase]:
            return v
        raise ValueError("Invalid genre")

    @field_validator("language")
    def check_categoria(cls, v):
        if v is None:
            return v
        if v in [item.value for item in LanguageBase]:
            return v
        raise ValueError("Invalid language")
