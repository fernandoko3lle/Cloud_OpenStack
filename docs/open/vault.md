### Configurar variável de ambiente

```bash
export VAULT_ADDR="http://172.16.0.55:8200"
```

### Inicialização do Vault

```bash
vault operator init -key-shares=5 -key-threshold=3
```

**Sample output:**

```
Unseal Key 1: XONSc5Ku8HJu+ix/zbzWhMvDTiPpwWX0W1X/e/J1Xixv
Unseal Key 2: J/fQCPvDeMFJT3WprfPy17gwvyPxcvf+GV751fTHUoN/
Unseal Key 3: +bRfX5HMISegsODqNZxvNcupQp/kYQuhsQ2XA+GamjY4
Unseal Key 4: FMRTPJwzykgXFQOl2XTupw2lfgLOXbbIep9wgi9jQ2ls
Unseal Key 5: 7rrxiIVQQWbDTJPMsqrZDKftD6JxJi6vFOlyC0KSabDB

Initial Root Token: s.ezlJjFw8ZDZO6KbkAkm605Qv

Vault initialized with 5 key shares and a key threshold of 3. Please securely
distribute the key shares printed above.
```

### Unseal do Vault

Utilize três chaves únicas para desbloquear o cofre:

```bash
vault operator unseal XONSc5Ku8HJu+ix/zbzWhMvDTiPpwWX0W1X/e/J1Xixv
vault operator unseal FMRTPJwzykgXFQOl2XTupw2lfgLOXbbIep9wgi9jQ2ls
vault operator unseal 7rrxiIVQQWbDTJPMsqrZDKftD6JxJi6vFOlyC0KSabDB
```

### Geração de Token Temporário

```bash
export VAULT_TOKEN="s.ezlJjFw8ZDZO6KbkAkm605Qv"
vault token create -ttl=10m
```

**Sample output:**

```
Key                  Value
---                  -----
token                s.QMhaOED3UGQ4MeH3fmGOpNED
token_accessor       nApB972Dp2lnTTIF5VXQqnnb
token_duration       10m
token_renewable      true
token_policies       ["root"]
policies             ["root"]
```

### Autorizar o Charm Vault

> **Atenção:** a partir da última versão do Juju, utilize `juju run` em vez de `juju run-action --wait`.

```bash
juju run vault/leader authorize-charm token=s.QMhaOED3UGQ4MeH3fmGOpNED
```

### Gerar Certificado CA

Para criar o **root CA** utilizado pelo Vault:

```bash
juju run vault/leader generate-root-ca
```

**Saída esperada:**  
`root_ca_cert` em base64 ou caminho para o arquivo `.pem`, usado para clientes confiáveis.

---

> Com estas etapas, o Vault está inicializado, desbloqueado, autorizado e pronto para emitir certificados, garantindo uma integração segura com seus serviços OpenStack.