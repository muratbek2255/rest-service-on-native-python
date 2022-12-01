import json
import socket
from datetime import date

import environs

env = environs.Env()

IP = env('HOST')
PORT = int(env('PORT'))


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
server.bind((IP, PORT))
server.listen(5)

while True:
    client, address = server.accept()
    print(f"Connection Established - {address[0]}: {address[1]}")

    body = client.recv(1024)
    body = body.decode("utf-8")
    parsed_data = json.loads(body)
    print(parsed_data['time'])
    print(type(parsed_data['time']))

    now_date = date.today()
    print(now_date)
    print(type(now_date))

    if parsed_data["time"] == str(now_date):
        print("Running name: ")
        print(parsed_data["name"])

        client.send(bytes(body, "utf-8"))

        client.close()
