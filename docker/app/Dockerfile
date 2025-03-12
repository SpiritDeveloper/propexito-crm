FROM python:3.9.10-alpine
ADD . /app
WORKDIR /app 

# You will need 
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev \
    && apk add g++ \
    && apk add mysql mysql-client netcat-openbsd

RUN echo "jenkins ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

COPY requirements.txt /app/
RUN pip install -r requirements.txt