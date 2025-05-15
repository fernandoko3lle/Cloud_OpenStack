## 1. Deploy dos Charms

Instalamos cada serviço a partir do canal estável correspondente:

```bash
# Armazenamento Ceph
juju deploy ceph-mon --channel quincy/stable --config auth-supported=none --num-units 3
juju deploy ceph-osd --channel quincy/stable --storage osd-devices=/dev/sdb

# Cinder e MySQL
juju deploy mysql-router --channel 8.0/stable
juju deploy cinder --channel victoria/stable
juju deploy cinder-mysql-router --channel 8.0/stable

# Object Storage
juju deploy ceph-radosgw --channel quincy/stable

# Serviços OpenStack
juju deploy glance --channel stein/stable
juju deploy keystone --channel victoria/stable
juju deploy rabbitmq-server --channel 3.8/stable
juju deploy placement --channel victoria/stable
juju deploy nova-cloud-controller --channel victoria/stable
juju deploy nova-compute --channel victoria/stable
juju deploy neutron-api --channel liberty/stable
juju deploy openstack-dashboard --channel victoria/stable

# Vault para segredos
juju deploy vault --channel 1.9/stable
juju deploy vault-mysql-router --channel 8.0/stable
```

---

## 2. Integração de Serviços com `juju integrate`

```bash
# Keystone ↔ RabbitMQ e MySQL
juju integrate keystone:identity-service rabbitmq-server:amqp
juju integrate keystone:identity-service mysql-router:db

# Glance ↔ Keystone
juju integrate glance:image-service keystone:identity-service

# Nova ↔ Placement e Keystone
juju integrate nova-cloud-controller:placement-api placement:placement-api
juju integrate nova-cloud-controller:identity-service keystone:identity-service

# Neutron ↔ Nova e RabbitMQ
juju integrate neutron-api:neutron-api rabbitmq-server:amqp
juju integrate neutron-api:cloud-compute nova-cloud-controller:cloud-compute

# Cinder ↔ MySQL e RabbitMQ
juju integrate cinder:db mysql-router:db
juju integrate cinder:amqp rabbitmq-server:amqp

# Vault ↔ MySQL (persistência)
juju integrate vault:mysql-router
```

---

