# Documentação – Projeto **Scraping B3 + Deploy AWS Lightsail**

---

## 1 · Explicação do Projeto — do Banco à API

Resumo cronológico das configurações para colocar a aplicação em produção no **AWS Lightsail**.

---

### 1.1 Criação do banco PostgreSQL

1. **Lightsail → Databases → Create database**  
2. Plano **Standard – 1 GB / 40 GB SSD / 2 vCPUs** (US $ 15/mês)  
3. Nome: `fastapi-db` · Usuário mestre: `dbkitH` · Porta: `5432`  
4. *Public mode* **Enabled** para testes iniciais.

| Evidência | Screenshot |
|-----------|------------|
| Banco recém‑criado | ![db_creation](../img/aws/db.png) |

---

### 1.2 Teste rápido de conectividade via CLI

Para garantir que o banco esta funcionando:

| Evidência | Screenshot |
|-----------|------------|
| Saída bem sucedida” | ![cli_port_test](../img/aws/teste_cli_db.png) |

---

### 1.3 Criação do serviço de contêiner

1. **Lightsail → Containers → Create container service**  
2. Nome: `fastapi-service` · Plano **Micro** (US $ 10/mês) · Escala: **1** instância

| Evidência | Screenshot |
|-----------|------------|
| Visão geral do contêiner | ![container_overview](../img/aws/fastAPI.png) |

---

### 1.5 Deploy da imagem Docker + variáveis de ambiente

| Item | Valor |
|------|-------|
| **Imagem** | `fernandokoelle/scraping_de_dados_b3:latest` |
| **Porta exposta** | `8000/TCP (HTTP)` |
| **Health‑check** | `/healthcheck` — HTTP 200 esperado |
| **Variáveis** | `DATABASE_URL=postgresql://dbkitH:***@ls-42e…amazonaws.com:5432/fastapi-db`<br>`SECRET_KEY=***` |

| Evidência | Screenshot |
|-----------|------------|
| Aba “Deploy” com imagem, porta e env vars | ![deploy_details](../img/aws/detalhes_deploy.png) |

---

## 2 · Como acessar a aplicação


Entre no link disponibilizado pelo conteiner da API e adicione a tag da FASTapi "/docs":
```bash
`https://fastapi-service.k2ztsvpymsmvg.us-east-1.cs.amazonlightsail.com/docs`
```

---

## 3 · Endpoints AWS Testados

| Endpoint | Verbo | Resultado | Screenshot |
|----------|-------|-----------|------------|
| `FAST`| DASHBOARD     | Overview      | ![dasboard Fast](../img/aws/dash_fast.png)
| `/healthcheck` | GET  | 200 OK        | ![health](../img/aws/hc.png) |
| `/login`       | POST | token JWT     | ![login](../img/aws/end_login.png) |
| `/registrar`   | POST | 201 Created   | ![registrar](../img/aws/end_registrar.png) |
| `/consultar`   | GET  | `[ … ]`       | ![consultar](../img/aws/end_consult.png) |

---

## 4 · Tela de Custos (dia da submissão)

<figure markdown>
<img src="../img/aws/custo_atual.png" width="700" alt="Custo atual">
<figcaption>Seção <strong>Billing &amp; usage</strong> em DD/MM/AAAA.</figcaption>
</figure>

* Projecões de custos mensais 

| Instâncias | Container (Micro) | Database 1 GB | **Total (USD/mês)** |
|------------|-------------------|---------------|---------------------|
| 1  | **US$ 10**  | **US$ 15** | **US$ 25** |
| 5  | **US$ 50**  | **US$ 15** | **US$ 65** |
| 10 | **US$ 100** | **US$ 15** | **US$ 115** |

---

## 5 · Vídeo de Execução (≤ 1 min)

[**▶️ Assista aqui** – INSIRA O LINK](https://youtu.be/6h7fCLQWV5k)

---
