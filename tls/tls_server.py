import json
import socket
import ssl
import environs

from datetime import date

env = environs.Env()

IP = env('HOST')
PORT = int(env('PORT'))


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
server.bind((IP, PORT))
server.listen(5)

while True:
    conn, addr = server.accept()
    server_ssl = ssl.wrap_socket(
        conn,
        server_side=True,
        certfile=env('Certfile'),
        keyfile=env('Keyfile'),
        ssl_version=ssl.PROTOCOL_TLSv1
    )

    try:
        while server_ssl:
            message = server_ssl.read()

            parsed_data = json.loads(message)
            print(parsed_data['time'])
            print(type(parsed_data['time']))

            now_date = str(date.today())
            print(now_date)
            print(type(now_date))

            if parsed_data["time"] == now_date:
                print("Running name: ")
                print(parsed_data["name"])

    except Exception as e:
        server_ssl.close()
        conn.close()
