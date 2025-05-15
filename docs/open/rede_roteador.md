# 🌐 Configurando Redes e Roteador

## Rede Externa `ext_net`

- **CIDR:** `172.16.0.0/20`
- **Pool de IPs flutuantes:** `172.16.7.0 – 172.16.8.255`
- **Gateway:** `172.16.0.1`
- **Tipo:** *flat* sobre `physnet1`

```bash
# Criar a rede externa compartilhada
openstack network create ext_net \
  --external \
  --share \
  --provider-network-type flat \
  --provider-physical-network physnet1

# Criar a sub-rede pública (sem DHCP)
openstack subnet create ext_subnet \
  --network ext_net \
  --no-dhcp \
  --gateway 172.16.0.1 \
  --subnet-range 172.16.0.0/20 \
  --allocation-pool start=172.16.7.0,end=172.16.8.255
```

---

## Rede Interna `int_net` + Roteador

- **CIDR interno:** `192.169.0.0/24`
- **Roteador:** `admin_router` (liga interna → externa)

```bash
# Criar rede privada para as VMs
openstack network create --internal int_net

# Criar sub-rede interna
openstack subnet create int_subnet \
  --network int_net \
  --subnet-range 192.169.0.0/24

# Criar roteador e conectar redes
openstack router create admin_router
openstack router add subnet admin_router int_subnet
openstack router set admin_router --external-gateway ext_net
```

---