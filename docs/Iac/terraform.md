
# Terraform – Infraestrutura-como-Código no Roteiro 4

## 1. Por que usar Terraform?

| Vantagem | Benefício prático no roteiro |
|----------|-----------------------------|
| **Automação** | Criação, alteração e destruição de recursos via `terraform apply` – sem cliques repetitivos no Horizon |
| **Idempotência** | Rodar várias vezes gera sempre o mesmo estado (útil para testes e rollback) |
| **Versionamento** | Os arquivos `.tf` entram no Git, permitindo PRs, _code review_ e auditoria |
| **Reprodutibilidade** | Outro colega/aluno pode clonar o repo, rodar `terraform init/apply` e obter a mesma topologia |
| **Plan before apply** | O comando `terraform plan` mostra diffs antes de alterar o ambiente, reduzindo erros |

---

## 2. Estrutura de Pastas adotada

```
terraform/
├── provider.tf
├── network.tf
├── router.tf
├── keypair.tf
├── instance1.tf
├── instance2.tf
└── floatingip.tf
```
---

## 3. Credenciais OpenStack (arquivo *RC*)

1. No Horizon, como **usuário do projeto do aluno**, baixe o **OpenStack RC file** (ex.: `myproject-openrc.sh`).  
2. **Problema observado:** quando fazíamos `source myproject-openrc.sh` direto, algumas variáveis entravam em conflito com variáveis herdadas da VM (`/etc/profile.d/openstack.sh`).  
3. **Solução adotada** – “limpar” primeiro o ambiente com o arquivo global e só então carregar o RC específico:

```bash
# 1) Exporta variáveis genéricas (usuário cloud)
source /home/cloud/openrc       # caminho padrão na VM teacher/cloud

# 2) Em seguida, exporta as variáveis do aluno/projeto
source ~/Downloads/myproject-openrc.sh
```

Isso garante que `OS_AUTH_URL`, `OS_USERNAME`, `OS_PROJECT_NAME`, etc. apontem para o **projeto correto** antes de chamar o Terraform.

---

## 4. Comandos-chave

```bash
cd terraform/

# Inicializa o diretório (baixar provider, criar .terraform)
terraform init

# Pré-visualiza mudanças no ambiente
terraform plan -out=tfplan

# Aplica as mudanças confirmadas
terraform apply tfplan
```

Se precisar desfazer:

```bash
terraform destroy
```

---

## 5. Código Terraform

<details>
<summary><code>floatingip.tf</code></summary>

```hcl
data "openstack_networking_network_v2" "ext" {
  name     = "ext_net"
  external = true
}

resource "openstack_networking_floatingip_v2" "fip_a" {
  pool = data.openstack_networking_network_v2.ext.name
}

resource "openstack_networking_floatingip_v2" "fip_b" {
  pool = data.openstack_networking_network_v2.ext.name
}

resource "openstack_compute_floatingip_associate_v2" "assoc_a" {
  floating_ip = openstack_networking_floatingip_v2.fip_a.address
  instance_id = openstack_compute_instance_v2.instancia_1.id
}

resource "openstack_compute_floatingip_associate_v2" "assoc_b" {
  floating_ip = openstack_networking_floatingip_v2.fip_b.address
  instance_id = openstack_compute_instance_v2.instancia_2.id
}
```
</details>

<details>
<summary><code>instance1.tf</code></summary>

```hcl
resource "openstack_compute_instance_v2" "instancia_1" {
  name            = "basic"
  image_name      = "jammy-amd64"
  flavor_name     = "m1.small"
  key_pair        = "my-keypair"
  security_groups = ["default"]

  network {
    name = "network_1"
  }

  depends_on = [openstack_networking_network_v2.network_1]

}
```
</details>

<details>
<summary><code>instance2.tf</code></summary>

```hcl
resource "openstack_compute_instance_v2" "instancia_2" {
  name            = "basic2"
  image_name      = "jammy-amd64"
  flavor_name     = "m1.tiny"
  key_pair        = "my-keypair"
  security_groups = ["default"]

  network {
    name = "network_1"
  }

  depends_on = [openstack_networking_network_v2.network_1]

}
```
</details>

<details>
<summary><code>keypair.tf</code></summary>

```hcl
  GNU nano 6.2                                                                keypair.tf                                                                         
resource "openstack_compute_keypair_v2" "test-keypair" {
  name = "my-keypair"
}
```
</details>

<details>
<summary><code>network.tf</code></summary>

```hcl
resource "openstack_networking_network_v2" "network_1" {
  name           = "network_1"
  admin_state_up = "true"
}

resource "openstack_networking_subnet_v2" "subnet_1" {
  network_id = "${openstack_networking_network_v2.network_1.id}"
  cidr       = "192.167.199.0/24"
}
```
</details>

<details>
<summary><code>provider.tf</code></summary>

```hcl
# Terraform Openstack deployment

# Define required providers
terraform {
required_version = ">= 0.14.0"
  required_providers {
    openstack = {
      source  = "terraform-provider-openstack/openstack"
      version = "~> 1.35.0"
    }
  }
}


# Configure the OpenStack Provider

provider "openstack" {
  region              = "RegionOne"
  user_name           = "FernandoKoelle"
}
```
</details>

<details>
<summary><code>router.tf</code></summary>

```hcl
resource "openstack_networking_router_v2" "router_1" {
  name                = "my_router_f"
  admin_state_up      = true
  external_network_id = "6795929c-ee09-4c30-864f-e70c5074e1a2"
}

resource "openstack_networking_router_interface_v2" "int_1" {
  router_id = "${openstack_networking_router_v2.router_1.id}"
  subnet_id = "${openstack_networking_subnet_v2.subnet_1.id}"
}
```
</details>

---