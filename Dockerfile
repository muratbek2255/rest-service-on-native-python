FROM python:3.9

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

EXPOSE 8888

RUN pip install -r requirements.txt

RUN export $(grep -v "^#" .env | xargs)

# if you wanna change on https or tcp, create: https/ . or tcp/ . and then change in CMD
COPY tls/ .

CMD [ "python", "./tls_server.py", "--max_conn=10", "--buffer_size=8192"]