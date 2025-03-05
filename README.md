# Python CRUD - Sistema de gerenciamento de livros

Este projeto é uma API CRUD (Create, Read, Update, Delete) simples desenvolvida em Python, projetada para ser executada em um ambiente Docker.

## Estrutura do projeto
- **Banco de Dados**: Utilizado o [PostgreSQL](https://hub.docker.com/_/postgres), com a imagem oficial do Docker, como nosso sistema de gerenciamento de banco de dados relacional.
- **Backend**: Desenvolvido com o ORM [SQLAlchemy](https://www.sqlalchemy.org/), que facilita a comunicação com o banco de dados. Para garantir a integridade dos dados, é utilizado o [Pydantic](https://docs.pydantic.dev/latest/) para validação de tipos. A API CRUD é construída com [FastAPI](https://fastapi.tiangolo.com/).
- **Frontend**: A interface de usuário para a API é criada usando [Streamlit](https://streamlit.io/).

## Como executar via Docker

Para executar este projeto utilizando Docker, siga as instruções abaixo:

1.  **Instale o Docker e o Docker Compose:**

    Certifique-se de que o Docker e o Docker Compose estejam instalados em seu sistema. Você pode baixá-los em:

    - [Docker](https://www.docker.com/get-started)
    - [Docker Compose](https://docs.docker.com/compose/install/)

2.  **Clone o repositório:**

    Clone este repositório para sua máquina local:

    ```bash
    git clone https://github.com/guilhermeaoliver/python_crud.git
    cd python_crud
    ```

3.  **Construa e execute os containers:**

    Utilize o Docker Compose para construir e executar os containers da aplicação:

    ```bash
    docker-compose up --build
    ```

    Este comando irá construir a imagem Docker e iniciar os containers definidos no arquivo `compose.yaml`.

4.  **Acesse as aplicações:**

    - Frontend: http://localhost:8501
    - Backend: http://localhost:8000/docs


## Observações

*   Certifique-se de que as portas 8000 e 8501 estejam disponível em sua máquina.
*   Para parar a execução dos containers, utilize o comando `docker-compose down`.
