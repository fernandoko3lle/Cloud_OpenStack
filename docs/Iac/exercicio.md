# Plano de Implantação de Sistema Crítico em **Public Cloud**

> **Contexto**  
> Você é o CTO de uma grande empresa com filiais em várias capitais brasileiras. Precisa implantar um sistema crítico, de baixo custo e com dados sigilosos para a área operacional.  
> A seguir encontram-se as respostas aos itens solicitados no exercício, já formatadas para uso direto no relatório.  

---

## 1. Escolha: **Public Cloud** ✅

| Critério                | Public Cloud | Private Cloud | Por que escolher Public? |
|-------------------------|--------------|---------------|--------------------------|
| **Custo inicial**       | Baixo CAPEX (modelo pay-as-you-go) | Alto CAPEX (compra de hardware) | Mantém o projeto dentro do orçamento, libera capital para P&D. |
| **Escalabilidade**      | Elástica, global, automática       | Limitada ao hardware próprio    | Suporta picos sazonais sem superprovisionar. |
| **Segurança**           | Data centers com compliance (ISO 27001, SOC 2, LGPD-ready); cifragem por padrão | Total controle físico, mas exige equipe dedicada | Serviços gerenciados de IAM, KMS e WAF reduzem risco humano. |
| **Time-to-market**      | Provisionamento em minutos         | Semanas/meses (aquisição e instalação) | Entrega mais rápida do valor de negócio. |
| **Alta disponibilidade**| Regiões e zonas de disponibilidade prontas | Requer sites redundantes | DR/HA “as a service”, menor complexidade operacional. |

> **Conclusão:** A Public Cloud atende aos requisitos de **baixo custo**, **escalabilidade** e **segurança** ao mesmo tempo — permitindo foco da equipe na lógica de negócio em vez de infraestrutura.

---

## 2. Por que precisamos de um time **DevOps**? 👥

| Responsabilidade DevOps | Benefício para a empresa | Rationale para RH |
|-------------------------|--------------------------|-------------------|
| **Automação de CI/CD**  | Releases frequentes, sem janelas de indisponibilidade | Menos retrabalho e menor tempo de aprovação de mudanças. |
| **Infraestrutura como Código (IaC)** | Configurações rastreáveis, auditáveis | Reduz erros manuais e facilita auditorias de segurança. |
| **Observability & SRE** | Monitoramento proativo, SLOs claros | Evita interrupções prolongadas e melhora a experiência do usuário. |
| **Cultura colaborativa**| Quebra silos Dev–Ops, acelera feedback | Retém talentos que buscam ambientes modernos e ágeis. |

> **Argumento para RH:** Um time DevOps alinha‐se à estratégia de negócios, diminuindo custos operacionais, aumentando a qualidade do software e reduzindo riscos de incidentes — impactando diretamente a receita e a satisfação do cliente.

---

## 3. Plano de **DR (Disaster Recovery)** e **HA (High Availability)** 🛡️

### 3.1 Mapeamento de Ameaças 🔍
| Categoria | Ameaça específica | Impacto potencial |
|-----------|------------------|-------------------|
| **Física** | Falha de data center regional | Interrupção total de serviços |
| **Lógica** | Erro de implantação (bug)     | Degradação de serviço / perda de dados |
| **Segurança** | Ransomware / vazamento LGPD | Multas e danos à reputação |
| **Operacional** | Falha humana em config. IAM | Acesso não autorizado |
| **Externa** | Ataques DDoS volumétricos     | Queda de disponibilidade |

### 3.2 Ações Prioritárias de Recuperação 🚑
1. **Fail-over automático** para zona secundária (≤ 1 min RTO).  
2. **Restauro point-in-time** de banco de dados ≤ 15 min RPO.  
3. **Infraestrutura como Código** para reprovisionar ambiente completo em < 1 h.  
4. **Runbooks de incidentes** versionados e testados em game days semestrais.  

### 3.3 Política de Backup 💾
| Item                | Estratégia |
|---------------------|------------|
| **Frequência**      | Snapshots horários + full daily |
| **Retenção**        | 35 dias em região primária; 90 dias em região cross-region |
| **Criptografia**    | At rest (KMS) e in transit (TLS 1.3) |
| **Teste de restore**| Mensal (automático) + semestral (auditado) |
| **Responsável**     | DevOps on-call (rota 24×7) |

### 3.4 Alta Disponibilidade (HA) ⚙️
- **Compute:** Auto-Scaling Groups em **2+ zonas** com balanceador (ALB).  
- **Database:** Pares Multi-AZ (PostgreSQL gerenciado) + réplicas de leitura.  
- **Cache/Queue:** Redis/MQ multi-node com redistribuição automática.  
- **Network:** Route 53 & Anycast DNS para fail-over geo-redundante.  
- **Observabilidade:** Métricas + logs centralizados em serviço gerenciado (Grafana/Loki).  

---

## 4. Cronograma de Implementação ⏱️
| Fase | Duração | Entregáveis |
|------|---------|-------------|
| **Kick-off & Acesso à Cloud** | 1 semana | Contas, landing zone, IAM baseline |
| **IaC & Pipelines CI/CD**     | 2 semanas | Repositórios Git, pipelines, testes |
| **MVP + HA**                  | 3 semanas | App em 2 zonas, banco Multi-AZ |
| **DR & Backups**              | 2 semanas | Rotinas de snapshot, cross-region |
| **Game Day & Hardening**      | 1 semana  | Testes de falha, revisão de segurança |
| **Go-live**                   | —         | Change freeze + monitoramento 24×7 |

---