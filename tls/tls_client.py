import json
import socket
import ssl
from datetime import date

import environs

env = environs.Env()

IP = env('HOST')
PORT = int(env('PORT'))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_ssl = ssl.wrap_socket(client, ca_certs="/home/murat/ssl2/certificate.pem")

client_ssl.connect((IP, PORT))

while True:
    date_entry = input('Enter a date in YYYY-MM-DD format: ')
    year, month, day = map(int, date_entry.split('-'))
    date1 = date(year, month, day)

    body = {
        "name": input("Write name: "),
        "time": str(date(year, month, day))
    }
    jsonResult = json.dumps(body).encode("utf-8")
    client_ssl.write(jsonResult)


client.close()
