# 🎯 Objetivo do Projeto OpenStack

Bem-vindo à documentação completa do nosso **projeto de Cloud Privada com OpenStack**! Este material apresenta, de forma prática e direta, todo o ciclo de vida da infraestrutura e dos serviços, desde a configuração inicial até a operação da aplicação.

## 🏗️ 1. Provisionamento de Infraestrutura

- Criamos instâncias de computação para executar nossos componentes: APIs, banco de dados e balanceador.
- Registramos imagens no Glance e definimos flavors adequados para cada função, equilibrando custo e performance.
- Atribuímos IPs internos e um IP flutuante para permitir acesso externo via NAT.

## 🌐 2. Configuração de Rede

- Configuramos uma rede interna isolada (CIDR `192.169.0.0/24`) para toda a comunicação entre serviços.
- Provisionamos um roteador que faz NAT de saída e mapeia o IP flutuante para o balanceador NGINX.
- Implementamos regras de NAT no roteador físico para acesso ao ambiente sem necessidade de túneis.

## ☁️ 3. Deploy do OpenStack

- Criamos projetos, usuários e atribuímos permissões no Keystone.
- Configuramos serviços essenciais (Nova, Neutron, Cinder, Glance) para fornecer IaaS.
- Garantimos que todos os componentes estejam interconectados e operacionais.

## 🚀 4. Deploy da Aplicação

- Containerizamos a API FastAPI, o PostgreSQL e o NGINX.
- Realizamos push das imagens no Docker Hub e consumimos-nas nas instâncias OpenStack.
- Configuramos o upstream do NGINX e o endpoint `/health_check` para monitoramento ativo.

## 🧪 5. Testes e Validação

- Acessamos o painel Horizon para verificar topologia e status das instâncias.
- Executamos chamadas HTTP a `/health_check` e `/docs` para confirmar disponibilidade e balanceamento.
- Analisamos logs e métricas para avaliar desempenho e resiliência.

## 🔒 6. Segurança e Boas Práticas

- Após a validação, removemos IPs públicos das VMs internas, mantendo apenas o roteador como ponto de exposição.
- Asseguramos que toda a comunicação entre serviços ocorra via rede interna.
- Aplicamos políticas de firewall e controles de segurança no Neutron e no roteador físico.

> **Objetivo principal:** proporcionar um **aprendizado prático** no uso do OpenStack, capacitando o leitor a configurar, operar e validar uma infraestrutura de nuvem privada de ponta a ponta.