# Setup do Ambiente – Domínio **AlunosAdmin**

## 1. Objetivos da Estrutura de Usuários

- **Isolamento de recursos**&nbsp;🔒  
  Cada aluno opera em seu próprio projeto para evitar colisões de redes, instâncias ou quotas.
- **Delegação de permissões** 👥  
  O papel *Member* é concedido apenas no projeto individual; tarefas administrativas ficam restritas ao *domainAdmin*.
- **Auditoria facilitada** 📑  
  Logs e métricas ficam segmentados por projeto, simplificando a cobrança (quota) e o troubleshooting.
- **Preparação para DevOps / IaC** ⚙️  
  A hierarquia Dominío → Projetos → Usuários reflete o que será usado no Terraform e em futuros pipelines CI/CD.

---

## 2. Passo-a-Passo no Dashboard (Horizon)

> Você precisará estar logado como **domainAdmin** (ou outro usuário com *Admin* no domínio *Default*).

| Etapa | Ação | Dica Visual |
|-------|------|-------------|
| **2.1** | *Identity → Domains → Create Domain* <br>• **Domain Name**: `AlunosAdmin` <br>• Enable: ✔️ | ![](images/horizon_create_domain.png) |
| **2.2** | Selecione o novo domínio `AlunosAdmin` <br>*Identity → Projects → Create Project* | (repita para cada aluno) |
| | • **Project Name**: `kit-<letra>-<aluno>`<br>• **Description**: “Projeto individual do roteiro 4” | |
| **2.3** | Ainda dentro de `AlunosAdmin` <br>*Identity → Users → Create User* | |
| | • **User Name**: `<aluno>` <br>• **Primary Project**: seu novo projeto <br>• **Password**: definir / enviar ao aluno | |
| **2.4** | Atribua papéis (*Manage Members*) | <br>• **Member** no projeto do aluno <br>• (Opcional) `reader` em outros projetos |
| **2.5** | **Teste rápido** <br> Logout → login como `<aluno>` | Deve enxergar **somente** o próprio projeto |

> ✅ *Checklist:* domínio criado, projetos individuais, usuários criados, cada usuário com acesso somente ao seu projeto.

---

## 3. Próximos Passos

1. Exportar o arquivo `openstack.rc` para cada usuário (via Horizon).  
2. Usar essas credenciais nos comandos CLI / Terraform.  
3. Conferir quotas (Compute, Network, Volume) e ajustar se necessário.

---
