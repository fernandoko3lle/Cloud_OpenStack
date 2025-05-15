
# ⚙️ Arquivo `docker-compose.yaml`

Este arquivo é responsável por orquestrar os três principais contêineres do projeto: **NGINX**, **FastAPI** e **PostgreSQL**. Ele define a forma como esses serviços interagem entre si e com o ambiente externo.

---

## 📂 Estrutura Geral

```yaml
name: cloud

services:
  web:
    image: fernandokoelle/nginx_proxy
    ports:
      - "8000:80"
    depends_on:
      - api
    restart: on-failure
  api:
    hostname: api
    image: fernandokoelle/scraping_de_dados_b3:latest
    environment:
      DATABASE_URL: postgresql://cloud:secret@db:5432/cloud
      SECRET_KEY: ${SECRET_KEY:-supersegredo}
      ADMIN_SECRET: ${ADMIN_SECRET:-123}
    depends_on:
      - db
    restart: on-failure
  
  db:
    hostname: db
    image: postgres:latest
    environment: 
      POSTGRES_DB: ${POSTGRES_DB:-cloud}
      POSTGRES_USER: ${POSTGRES_USER:-cloud}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-secret}
    restart: on-failure

```

---

## 🔁 Ordem de Inicialização

1. O serviço `db` é iniciado primeiro (PostgreSQL).
2. Em seguida, a `api`, que depende do banco de dados para iniciar corretamente.
3. Por fim, o `web`, que age como **proxy reverso**, redirecionando as requisições da porta 8000 para a API.

---

## 🔍 Explicação de cada serviço:

### 🧭 `web` (NGINX Proxy)
- Função: redirecionar requisições externas para a API.
- Porta exposta: `8000 -> 80`.

### 🧠 `api` (FastAPI)
- Responsável por processar requisições, autenticar usuários e interagir com o banco de dados.
- Usa variáveis de ambiente para configuração.

### 🧱 `db` (PostgreSQL)
- Banco de dados da aplicação.
- Usa senha e nome de banco definidos no `.env`.

---

## 🔐 Segurança e Produção

- Nunca exponha portas desnecessárias. Somente a porta `8000` está visível neste projeto.
- As credenciais sensíveis estão externalizadas via `.env`, não deixe esse arquivo público.
- Utilize imagens validadas no Docker Hub para ambientes de produção.

---

## ✍️ Dicas de Customização

- Para rodar em uma porta diferente, altere `8000:80` para `sua_porta:80` na seção `web`.
- Você pode adicionar um volume para persistência dos dados do banco, se desejar.
- Para logar e testar, acesse `http://localhost:8000/docs` no navegador.

---