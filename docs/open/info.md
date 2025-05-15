
# ☁️ Implantação no OpenStack e Arquitetura da Solução

Este documento detalha o processo de implantação da infraestrutura e da aplicação em um ambiente OpenStack. A solução foi estruturada para refletir um ambiente realista de produção, com separação clara de responsabilidades entre serviços e instâncias.

---

## 🌐 Topologia de Rede

A arquitetura da aplicação foi desenhada de forma a separar os componentes em três camadas principais:

- **Load Balancer (NGINX)**: responsável por distribuir as requisições entre as instâncias da API.
- **API**: duas instâncias idênticas da aplicação desenvolvida com FastAPI.
- **Banco de Dados**: uma instância com PostgreSQL, isolada das demais para segurança.

> 💡 *Imagem com a topologia será inserida aqui.*

A rede utilizada para a comunicação entre as instâncias foi `192.169.0.0/24`, com roteamento NAT configurado para saída externa via IP flutuante.

---

## ⚖️ Load Balancer e Rota `/health_check`

O balanceamento de carga foi implementado utilizando o NGINX como proxy reverso, configurado para rotear as requisições entre as APIs `api-1` e `api-2`.

- O arquivo `nginx.conf` define um bloco `upstream` com os nomes das instâncias registrados no arquivo `/etc/hosts`.
- A rota `/health_check` foi adicionada na API para permitir verificação ativa de qual instância está respondendo.

### Exemplo de resposta da rota `/health_check`:

```json
{
  "status": "ok",
  "instance": "api-1"
}
```

Essa abordagem permite acompanhar se o balanceamento está funcionando corretamente.

---

## 🧠 Escolha dos Flavors

Os flavors foram selecionados com base na função de cada instância:

| Instância     | Função            | Flavor   | Motivo da Escolha                          |
|---------------|-------------------|----------|--------------------------------------------|
| `api-1`       | API               | `m1.tiny`| Leve, suficiente para servir requisições.  |
| `api-2`       | API               | `m1.tiny`| Reforço à alta disponibilidade.            |
| `db-server`   | Banco de Dados    | `m1.small`| Memória extra para operações SQL.         |
| `lb-nginx`    | Load Balancer     | `m1.tiny`| Responsável apenas pelo encaminhamento.   |

> A escolha privilegia o **custo-benefício**, mantendo o sistema funcional com o menor uso de recursos possível.

---

## 🚀 Subida das Instâncias e Configuração de IPs

As instâncias foram criadas via terminal com o comando `openstack server create` e associadas a IPs flutuantes.

### Comandos utilizados

```bash
openstack server create --flavor m1.tiny --image jammy-amd64 \
  --nic net-id=<id_rede_interna> --security-group default \
  --key-name minha-chave api-1

openstack floating ip create ext_net
openstack server add floating ip api-1 <ip_flutuante>
```

### Resultado:

| Instância   | IP Interno     | IP Flutuante      |
|-------------|----------------|-------------------|
| `api-1`     | 192.169.0.220   | 172.16.0.34       |
| `api-2`     | 192.169.0.134   | 172.16.0.198      |
| `db-server` | 192.169.0.168   | 172.16.7.1        |
| `lb-nginx`  | 192.169.0.15    | 172.16.8.94       |

> As regras de NAT foram criadas no roteador da rede, redirecionando a porta 8000 para a porta 80 do container NGINX.

---

*Este documento será posteriormente dividido em seções específicas no MkDocs.*