# p1fullstack

Projeto da disciplina **Laboratório de Programação Full Stack** — Engenharia de Software, Universidade de Vassouras.

## Sobre o projeto

Sistema de biblioteca (app `acervo`) construído a partir do consolidado das atividades práticas de:

- **Aula 4 — Django na Prática I**: ambiente virtual, criação do projeto/app, model `Livro`, migrações e Django Admin.
- **Aula 5 — Django na Prática II**: views, URLs, templates com herança, arquivos estáticos e formulários (`ModelForm`).

## Funcionalidades

- Cadastro, edição e exclusão de livros (CRUD completo).
- Classificação do acervo por **tipo** (Digital ou Físico).
- Classificação por **categoria**, seguindo a Classificação Decimal Universal (CDU):
  - 000 – Generalidades e Informação
  - 100 – Filosofia e Psicologia
  - 200 – Religião e Teologia
  - 300 – Ciências Sociais e Direito
  - 400 – Linguística e Idiomas
  - 500 – Ciências Puras (Exatas e Naturais)
  - 600 – Ciências Aplicadas (Tecnologia)
  - 700 – Artes e Recreação
  - 800 – Literatura
  - 900 – História e Geografia
- Pesquisa do acervo por nome (título/autor), tipo e categoria.

## Como rodar

```bash
python -m venv venv
venv\Scripts\activate        # Windows
pip install django python-dotenv
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acesse `http://127.0.0.1:8000/livros/` para a lista pública e `http://127.0.0.1:8000/admin/` para o painel administrativo.
