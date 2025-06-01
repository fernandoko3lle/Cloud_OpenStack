## 1.1 Escolha da Plataforma de Cloud  

**Decisão:** **Public Cloud (modelo Multi-AZ)**  

| Requisito          | Como é atendido no Public Cloud | Observações de implementação |
|--------------------|---------------------------------|------------------------------|
| **Alta segurança** | • Criptografia AES-256 em repouso e TLS 1.3 em trânsito (KMS/HSM)<br>• Redes privadas (VPC), sub-redes sem acesso público, VPN/Direct Connect para escritórios e fábricas<br>• Certificações ISO 27001, SOC 2, PCI-DSS, LGPD-ready<br>• IAM com MFA obrigatório e política **least-privilege** | Adotar DevSecOps: _Secrets Manager_, _WAF/Shield_ contra DDoS, escaneamentos de imagem e código no pipeline |
| **Escalabilidade** | • Auto-Scaling horizontal de contêineres/Kubernetes<br>• Serviços gerenciados (RDS, S3, ElastiCache) que escalam vertical e horizontalmente sob demanda<br>• Backbones de alta capacidade entre regiões brasileiras | Definir _SLOs_ (latência p95, throughput) para ajustar políticas de scaling; usar _Spot_ para cargas tolerantes a interrupção |
| **Custo-benefício**| • Modelo **pay-as-you-go** evita CapEx pesado<br>• _Reserved Instances_ / _Savings Plans_ reduzem até 60 % do Opex<br>• Serverless elimina ociosidade em horários de baixa | Implantar práticas de **FinOps**: tagging, budgets, alertas de custo e _rightsizing_ contínuo |

> **Nota técnica:** Se alguma regulação exigir segregação física extrema, coloque apenas os workloads **ultra-sigilosos** em uma extensão on-prem (Ex.: AWS Outposts, Google Anthos, colocation) e mantenha o restante no Public Cloud — aproximando-se de um **modelo híbrido focalizado** que conserva ganhos de escala e economia.

### Próximos Passos
1. Arquitetar a solução seguindo o _Well-Architected Framework_ do provedor.  
2. Automatizar a infraestrutura com Terraform/Ansible (_Infrastructure as Code_).  
3. Configurar **DR & HA** multi-AZ (e opcionalmente multi-region) com RTO ≤ 15 min e RPO ≤ 5 min.  
4. Implantar observabilidade 360 ° (logs centralizados, métricas Prometheus/Grafana, tracing).  
5. Conduzir _Proof of Concept_ e _Security Assessment_ antes do “go-live”.  
