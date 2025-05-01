# 📊 Documentação - API de Scraping B3 com Autenticação JWT

Este projeto consiste em uma API RESTful desenvolvida com FastAPI, que realiza scraping de dados da B3 (Bolsa de Valores do Brasil) e disponibiliza os dados para usuários autenticados via JWT.

---

## 🔍 Explicação do Projeto

O sistema realiza scraping dos dados da B3 com informações como data, abertura, fechamento, volume, entre outros.

- Linguagem principal: **Python**
- Framework: **FastAPI**
- Containerização com **Docker**
- Banco de dados: **PostgreSQL**
- Balanceamento e proxy reverso com **NGINX**

---

## 📦 Endpoints da API

| Método | Rota         | Descrição                     |
|--------|--------------|-------------------------------|
| POST   | `/registrar` | Cria novo usuário             |
| POST   | `/login`     | Retorna token JWT             |
| GET    | `/consultar` | Consulta dados (requer JWT)   |


---

## 📂 Estrutura do Projeto

```
Cloud_OpenStack/
├── api_rest/
│   ├── api/
│   │   ├── app/
│   │   │   ├── app.py
│   │   │   ├── auth.py
│   │   │   ├── database.py
│   │   │   ├── models.py
│   │   │   ├── schemas.py
│   │   │   └── scraping.py
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   ├── nginx/
│   │   ├── Dockerfile
│   │   └── default.conf
│   ├── .env
│   └── docker-compose.yaml
```

---

## 🎥 Vídeo

- [Demonstração curta do funcionamento](https://youtu.be/vVhMcYC5w3g)

---