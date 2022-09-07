![FastApiCRUD](https://user-images.githubusercontent.com/94191697/188949992-f580d84e-97f6-440f-bb26-b6313de99988.png)


## CRUD FastApi
 
CRUD (Create, Read, Update, Delete) com FastApi usando PostgreSQL
 
 
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
* Criar e conectar usuário no banco de dados 
* Criar tabela e conectar na base de dados
* Criar tabela com os campos:
>    CREATE TABLE "user"(id serial PRIMARY KEY, name VARCHAR(100) NOT NULL, phone VARCHAR(10) NOT NULL);

## Executar Projeto
 
> uvicorn main:app --reload
* Documentação 
> localhot:8000/docs
 
 
## Versão
 
1.0.0.0
 
 
## Autor
 
* **Cristian Vitor**: @cristianvitor01 (https://github.com/cristianvitor01)
 
 

Obrigado por visitar ;)
