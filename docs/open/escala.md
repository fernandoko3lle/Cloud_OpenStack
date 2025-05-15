# 📈 Escalabilidade dos Nós

Escalar nós de **computação** e **block storage** no OpenStack amplia a capacidade, resiliência e desempenho do ambiente de nuvem.

---

## 🔑 Pontos‑chave

- **Capacidade de Processamento**  
  Aumento do número de instâncias simultâneas, atendendo mais usuários e aplicações.

- **Alta Disponibilidade (HA)**  
  Distribuição de cargas entre múltiplos nós reduz o impacto de falhas.

- **Desempenho e Latência**  
  Dados e processos mais próximos das VMs diminuem tempo de acesso.

- **Escalabilidade Horizontal**  
  Adicionar máquinas (versus “engordar” uma só) é mais econômico e simples de gerenciar; serviços como **Nova** e **Ceph** balanceiam cargas automaticamente.

---

## 🛠️ Comandos Utilizados

| Ação                                     | Comando |
|-----------------------------------------|---------|
| Adicionar novo nó de **compute**        | `juju add-unit nova-compute` |
| Instalar **block storage** (Ceph OSD)   | `juju add-unit --to <machine-id> ceph-osd` |

> **Passos prévios**  
> 1. Verificar no Dashboard do **MAAS** se há máquina **Allocated**.  
> 2. Fazer *release* da máquina para deixá‑la livre antes do deploy.

---

## Status do JUJU após a inserção do node:

![status apos node](../img/open/status_pos_node.png) 

## 🖼️ Diagrama de Rede (Insper → Instância)

```mermaid
flowchart TB
    %% Nós principais
    Insper["📶 Estação de Trabalho"]
    Roteador["🛣️ Roteador Físico"]

    subgraph "."
        direction TB
        NginxLB["🛡️ NGINX Load Balancer"]
        API1["🐳 VM api-1"]
        API2["🐳 VM api-2"]
        DB["🗄️ VM database"]
        TESTE("🌐 (192.169.0.0/24)")
    end 
    %% Conexões externas
    Insper e1@==>|VPN / Ethernet<br/>172.16.0.0/20| Roteador
    Roteador e2@==>|NAT Externo| NginxLB

    %% Conexões internas (tracejadas)
    NginxLB e3@==>|80 /TCP| API1
    NginxLB e4@==>|80 /TCP| API2
    API1 e5@==>|5432 /TCP| DB
    API2 e6@==>|5432 /TCP| DB



    e1@{ animate: true }
    e2@{ animate: true }
    e3@{ animate: true }
    e4@{ animate: true }
    e5@{ animate: true }
    e6@{ animate: true }


    %% Afinar as setas
    linkStyle default stroke-width:1px
```

---

