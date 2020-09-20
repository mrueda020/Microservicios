#Instalamos el S.O en esta caso Alpine
FROM alpine:3.12

#Instalamos python3 junto con pip
RUN apk add --no-cache python3-dev \
    && apk add py3-pip

#Se crea carpeta para guardar el codigo
WORKDIR /APIAPP

#Copiamos el codigo a la carpeta
COPY . /APIAPP

#Instalamos las dependencias de flask
RUN pip install --no-cache-dir install -r requisitos.txt

#Corremos la aplicacion
CMD ["python3","API/main.py"]

