FROM python:3.8-alpine
# Используем alpine, так как он весит меньше
# Немного информации о контейнере 
LABEL maintainer="вставьсюдысвоюпочту"
LABEL version="1.0"
LABEL description = "Vali Pautina crm service"
# Надо для питонских модулей
RUN apk add postgresql-client
RUN apk add postgresql-dev
# Надо для компиляции модулей
#RUN apt-get install scp
RUN apk add gcc
RUN apk add nano
RUN apk add g++
RUN apk add musl-dev
COPY . /My_QR_code/
WORKDIR /My_QR_code
# Ставим модули
RUN pip3 install -r requirements.txt

# Наконец, запускаем сервер 
CMD ['python3', 'wsgi.py']