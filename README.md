## CRUD FastApi
 
CRUDE (Create, Read, Update, Delete) com FastApi usando PostgreSQL
 
 
## Tecnologia 
 
* Python 3.10.4
* FastApi 0.82.0
 
## Serviços Usados
 
* Github
* PostgreSQL 14.5
 
## Para Começar
 
* Em seu ambiente virtual instalar fastapi, uvicorn, autopep8
>    pip install fastapi uvicorn autopep8
* Intalar psycopg 
>    pip install psycopg
* Criar e conectar Usuário no banco de dados 
* Criar tabela e conectar na base de dados
* Criar tabela com os campos:
>    CREATE TABLE "user"(id serial PRIMARY KEY, name VARCHAR(100) NOT NULL, phone VARCHAR(10) NOT NULL);

## Rodar Projeto
 
> uvicorn main:app --reload
 
 
## Versão
 
1.0.0.0
 
 
## Autor
 
* **Cristian Vitor**: @cristianvitor01 (https://github.com/cristianvitor01)
 
 

Obrigado por visitar ;)