FROM wardsco/sleep

# Actualiza los repositorios de paquetes y agrega herramientas de red
RUN apk update && \
    apk add --no-cache iputils curl wget net-tools bind-tools busybox-extras

# Comando por defecto para el contenedor
CMD ["trap : TERM INT; sleep infinity & wait"]