# Imagem do site estático servido por nginx.
# É esta imagem que o Trivy escaneia em busca de CVEs (slide 2: "imagem com CVE crítico").
# Tag fixada para o build ser reproduzível.
FROM nginx:1.27-alpine

# Copia o site para o diretório servido pelo nginx
COPY site/ /usr/share/nginx/html/

EXPOSE 80

# nginx:alpine já sobe o servidor via entrypoint padrão
