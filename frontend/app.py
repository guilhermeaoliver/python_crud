import streamlit as st
import requests
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns([1, 3], vertical_alignment="center")

with col1:
    st.image("logo.png", width=256)

with col2:
    st.title("Book Management System")

def show_response_message(response):
    if response.status_code == 200:
        st.success("Success")
    else:
        try:
            data = response.json()
            if "detail" in data:
                if isinstance(data["detail"], list):
                    errors = "\n".join([error["msg"] for error in data["detail"]])
                    st.error(f"Error: {errors}")
                else:
                    st.error(f"Error: {data['detail']}")
        except ValueError:
            st.error("Unknown error")


# Cadastrar livro
with st.expander("Register new book"):
    with st.form("new_book"):

        title = st.text_input("Title")
        author = st.text_input("Author")
        isbn = st.text_input("ISBN")
        publisher = st.text_input("Publisher")
        genre = st.selectbox(
            "Genre",
            ["Adventure", "Biography", "Children's", "Classics", "Crime", "Drama", "Dystopian", "Fantasy", 
             "Fiction", "Graphic Novels", "Historical Fiction", "Horror", "Humor", "Memoir", "Mystery", 
             "Non-fiction", "Poetry", "Romance", "Science Fiction", "Self-Help", "Spirituality", "Thriller",
             "Travel", "Western", "Young Adult", "Other"]
        )
        page_count = st.number_input("Page Count", min_value=1, format="%d")
        language = st.selectbox(
            "Language",
            ["Arabic", "Bengali", "Egyptian Arabic", "English", "French", "German", "Hausa", "Hindi", "Italian", 
             "Japanese", "Javanese", "Korean", "Mandarin Chinese", "Marathi", "Portuguese", "Russian", "Spanish", 
             "Tamil", "Telugu", "Turkish", "Urdu", "Vietnamese", "Western Punjabi", "Wu Chinese", "Yue Chinese (Cantonese)", 
             "Other"]
        )
        description = st.text_area("Description")
        price = st.number_input("Price", min_value=0.01, format="%f")

        submit_button = st.form_submit_button("Register Book")
        if submit_button:
            response = requests.post(
                "http://backend:8000/books/",
                json={
                    "title": title,
                    "author": author,
                    "isbn": isbn,
                    "publisher": publisher,
                    "genre": genre,
                    "page_count": page_count,
                    "language": language,
                    "description": description,
                    "price": price,
                },
            )
            show_response_message(response)

# Visualizar livros
with st.expander("View books"):
    if st.button("View all books"):
        response = requests.get("http://backend:8000/books/")
        if response.status_code == 200:
            book = response.json()
            df = pd.DataFrame(book)
            df = df[
                [
                    "id",
                    "title",
                    "author",
                    "isbn",
                    "publisher",
                    "genre",
                    "page_count",
                    "language",
                    "description",
                    "price",
                    "created_at",
                ]
            ]
            st.write(df.to_html(index=False), unsafe_allow_html=True)
        else:
            show_response_message(response)

# Visualizar um livro
with st.expander("Search for a book"):
    get_id = st.number_input("Book ID", min_value=1, format="%d")
    if st.button("Search book"):
        response = requests.get(f"http://backend:8000/books/{get_id}")
        if response.status_code == 200:
            book = response.json()
            df = pd.DataFrame([book])
            df = df[
                [
                    "id",
                    "title",
                    "author",
                    "isbn",
                    "publisher",
                    "genre",
                    "page_count",
                    "language",
                    "description",
                    "price",
                    "created_at",
                ]
            ]
            st.write(df.to_html(index=False), unsafe_allow_html=True)
        else:
            show_response_message(response)

# Excluir livro
with st.expander("Delete book"):
    delete_id = st.number_input("Book ID for deletion", min_value=1, format="%d")
    if st.button("Delete book"):
        response = requests.delete(f"http://backend:8000/books/{delete_id}")
        show_response_message(response)

# Atualizar livro
with st.expander("Update book"):
    with st.form("update_book"):
        update_id = st.number_input("Book ID for update", min_value=1, format="%d")

        new_title = st.text_input("New title")
        new_author = st.text_input("New author")
        new_isbn = st.text_input("New ISBN")
        new_publisher = st.text_input("New publisher")
        new_genre = st.selectbox(
            "New genre",
            ["Adventure", "Biography", "Children's", "Classics", "Crime", "Drama", "Dystopian", "Fantasy", 
             "Fiction", "Graphic Novels", "Historical Fiction", "Horror", "Humor", "Memoir", "Mystery", 
             "Non-fiction", "Poetry", "Romance", "Science Fiction", "Self-Help", "Spirituality", "Thriller",
             "Travel", "Western", "Young Adult", "Other"]
        )
        new_page_count = st.number_input("New page count", min_value=1, format="%d")
        new_language = st.selectbox(
            "New language",
            ["Arabic", "Bengali", "Egyptian Arabic", "English", "French", "German", "Hausa", "Hindi", "Italian", 
             "Japanese", "Javanese", "Korean", "Mandarin Chinese", "Marathi", "Portuguese", "Russian", "Spanish", 
             "Tamil", "Telugu", "Turkish", "Urdu", "Vietnamese", "Western Punjabi", "Wu Chinese", "Yue Chinese (Cantonese)", 
             "Other"]
        )
        new_description = st.text_area("New description")
        new_price = st.number_input("New price", min_value=0.01, format="%f")

        update_button = st.form_submit_button("Update book")

        if update_button:
            update_data = {}
            if new_title:
                update_data["title"] = new_title
            if new_author:
                update_data["author"] = new_author
            if new_isbn:
                update_data["isbn"] = new_isbn
            if new_publisher:
                update_data["publisher"] = new_publisher
            if new_genre:
                update_data["genre"] = new_genre
            if new_page_count:
                update_data["page_count"] = new_page_count
            if new_language:
                update_data["language"] = new_language
            if new_description:
                update_data["description"] = new_description
            if new_price > 0:
                update_data["price"] = new_price

            if update_data:
                response = requests.put(
                    f"http://backend:8000/books/{update_id}", json=update_data
                )
                show_response_message(response)
            else:
                st.error("No data to update")
