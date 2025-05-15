Confirmamos o estado de todos os serviços:

```bash
watch -n 1 --color "juju status --color"
```

Na saída, **Apps** devem estar `active/idle` e o **Vault** sem bloqueio.

![Status do Juju](../img/open/status_pre_node.png)  

O Dashboard do **MaaS** Após a criação da infraestrutura: 

![Status do MaaS](../img/open/tarefas/maas_pre_node.jpeg)  