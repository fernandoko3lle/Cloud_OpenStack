## 🎬 Subindo a Aplicação

### 1. Flavors das Instâncias

| Instância     | Função            | Flavor    | Motivo da Escolha                         |
|---------------|-------------------|-----------|-------------------------------------------|
| `api-1`       | API               | `m1.tiny` | Leve, suficiente para servir requisições. |
| `api-2`       | API               | `m1.tiny` | Reforço à alta disponibilidade.           |
| `db-server`   | Banco de Dados    | `m1.small`| Memória extra para operações SQL.         |
| `lb-nginx`    | Load Balancer     | `m1.tiny` | Responsável apenas pelo encaminhamento.   |

> A escolha privilegia o **custo-benefício**, mantendo o sistema funcional com o menor uso de recursos possível.

---

### 2. Criação das Instâncias e Atribuição de IPs

As instâncias foram criadas via CLI do OpenStack:

```bash
openstack server create --image jammy-amd64 \
  --flavor <FLAVOR> \
  --key-name admin \
  --network int_net \
  <NOME_INSTANCIA>
```

Em seguida, associamos IPs flutuantes para testes iniciais:

```bash
FLOATING_IP=$(openstack floating ip create -f value -c floating_ip_address ext_net)
openstack server add floating ip <NOME_INSTANCIA> $FLOATING_IP
```

#### Endereços atribuídos

| Instância   | IP Interno      | IP Flutuante     |
|-------------|-----------------|------------------|
| `api-1`     | 192.169.0.220   | 172.16.0.34      |
| `api-2`     | 192.169.0.134   | 172.16.0.198     |
| `db-server` | 192.169.0.168   | 172.16.7.1       |
| `lb-nginx`  | 192.169.0.15    | 172.16.8.94      |

---

### 3. Provisionamento da Aplicação

Para configurar cada instância:

1. **SSH**: conecte-se usando sua chave privada:
   ```bash
   ssh -i ~/cloud-keys/admin-key ubuntu@<IP_FLUTUANTE>
   ```
2. **Instalação do Docker**:
   ```bash
   sudo apt update
   sudo apt install -y docker.io
   sudo usermod -aG docker $USER
   ```
3. **Pull das imagens Docker**:
   ```bash
   docker pull <SEU_REPO>/api:latest
   docker pull <SEU_REPO>/database:latest
   docker pull <SEU_REPO>/lb-nginx:latest
   ```
4. **Inicialização dos containers**:
   ```bash
   docker run -d --name api-1 \
     -p 8000:8000 \
     <SEU_REPO>/api:latest
   # Repita em api-2, db-server e lb-nginx conforme necessário.
   ```

> **Observação**: detalhes de configuração de NGINX e regras de NAT estão documentados nas seções de Load Balancer e Topologia de Rede.