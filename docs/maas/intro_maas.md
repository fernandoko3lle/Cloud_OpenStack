# ☁️ Introdução ao MAAS

O **MAAS (Metal as a Service)** é uma ferramenta da Canonical que transforma hardware físico em uma nuvem privada, automatizando o provisionamento, o gerenciamento e a liberação de máquinas bare-metal.

De forma prática, o MAAS permite:

- **Descoberta automática** de servidores conectados à rede via PXE.
- **Provisionamento rápido** de sistemas operacionais (Ubuntu, CentOS, etc.) em máquinas físicas.
- **Gerenciamento centralizado** de ciclos de vida: desde a instalação até a liberação e reutilização dos recursos.

Em um cenário de **cloud privada**, o MAAS atua como a camada de IaaS que fornece instâncias bare-metal prontas para hospedar serviços críticos (como OpenStack, bancos de dados e balanceadores), garantindo controle total sobre hardware, performance dedicada e alta disponibilidade.

> **Objetivo desta seção:** demonstrar como utilizar o MAAS para provisionar e gerenciar servidores físicos, preparando o ambiente para a implantação de uma nuvem privada completa.