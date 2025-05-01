# 📤 Publicação no Docker Hub

A publicação das imagens Docker foi feita via linha de comando, conforme instruções da entrega. As imagens estão disponíveis publicamente no Docker Hub:

- 🔗 API: [fernandokoelle/scraping_de_dados_b3](https://hub.docker.com/r/fernandokoelle/scraping_de_dados_b3)
- 🔗 NGINX Proxy: [fernandokoelle/nginx_proxy_cloud](https://hub.docker.com/r/fernandokoelle/nginx_proxy_cloud)

---

## 🔧 Comandos utilizados

### 1. Acesse o diretório da API:

```bash
cd api_rest/api
```

### 2. Build da imagem da API

```bash
docker build -t fernandokoelle/scraping_de_dados_b3 .
```

### 3. Push da imagem da API

```bash
docker push fernandokoelle/scraping_de_dados_b3
```

### 4. Acesse o diretório do NGINX:

```bash
cd ../nginx
```

### 5. Build da imagem do NGINX

```bash
docker build -t fernandokoelle/nginx_proxy_cloud .
```

### 6. Push da imagem do NGINX

```bash
docker push fernandokoelle/nginx_proxy_cloud
```

---

!!! warning "Atenção"
    - Certifique-se de estar logado com `docker login` antes de fazer o push.
    - As imagens são utilizadas diretamente no `docker-compose.yaml`, sem etapas de build no compose.