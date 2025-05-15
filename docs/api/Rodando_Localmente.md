
# 🚀 Como Rodar Localmente

Siga os passos abaixo para clonar o projeto, configurar suas variáveis de ambiente e executar a aplicação via Docker Compose.

---

### 🔁 1. Clone o Repositório

Abra seu terminal e execute:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

---

### ⚙️ 2. Configure o Ambiente

Crie e edite o arquivo `.env` com as seguintes variáveis (exemplo abaixo):

```bash
SECRET_KEY=123
POSTGRES_USER=123
POSTGRES_PASSWORD=123
POSTGRES_DB=123
DATABASE_URL=postgresql://cloud:secret@db:5432/cloud
ADMIN_SECRET=123
```

> ⚠️ **Importante:** essas credenciais são usadas apenas para fins de aprendizado. Em produção, utilize valores seguros!

---

??? note "📁 Entenda + sobre a variável de Ambiente `DATABASE_URL`"
    A variável `DATABASE_URL` é essencial para a comunicação entre a aplicação FastAPI e o banco de dados PostgreSQL dentro do ambiente Docker Compose. Ela define os parâmetros necessários para a conexão com o banco de dados.

    ---

    ## 🧪 Estrutura do Valor

    ```env
    DATABASE_URL=postgresql://cloud:secret@db:5432/cloud
    ```

    ---

    ### 🔍 Explicação

    | Parte                           | Significado                                                                 |
    |--------------------------------|----------------------------------------------------------------------------|
    | `postgresql://`                | Define o tipo do banco de dados utilizado. Neste caso, PostgreSQL.         |
    | `cloud:`                       | Nome do usuário do banco de dados.                                         |
    | `secret@`                      | Senha do banco de dados correspondente ao usuário.                         |
    | `db:`                          | Hostname do serviço de banco de dados (nome do container Docker).          |
    | `5432`                         | Porta padrão utilizada pelo PostgreSQL.                                    |
    | `/cloud`                       | Nome do banco de dados que será acessado pela aplicação.                   |

    ---

    ## 🧱 Importância

    Essa variável evita que credenciais sensíveis fiquem hardcoded no código-fonte e permite a personalização do ambiente via `.env`, promovendo maior **segurança**, **flexibilidade** e **portabilidade** entre ambientes (desenvolvimento, staging, produção...).

    ---

    ## 📌 Observações

    - O nome `db` corresponde ao nome do serviço no `docker-compose.yaml`.
    - Todos os valores (usuário, senha, host e nome do banco) devem coincidir com os definidos no serviço `db`.
    
---

🔐 Manter essas credenciais protegidas é fundamental para a segurança da sua aplicação!

---

### 🛠️ 3. Construa os Contêineres

Execute o comando para construir as imagens Docker:

```bash
docker compose build
```

---

### ▶️ 4. Suba a Aplicação

Inicie todos os serviços com:

```bash
docker compose up
```

---

### 🌐 Acesse no Navegador

A aplicação estará disponível em:

```
http://localhost:8000/docs
```

> Utilize a interface interativa da FastAPI para testar os endpoints.