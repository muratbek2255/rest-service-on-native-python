import json
import socket
from datetime import datetime, date

import environs

env = environs.Env()

IP = env('HOST')
PORT = int(env('PORT'))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
server.connect((IP, PORT))

date_entry = input('Enter a date in YYYY-MM-DD format: ')
year, month, day = map(int, date_entry.split('-'))
date1 = datetime(year, month, day)

body = {
    "name": input("Write name: "),
    "time": str(date(year, month, day))
}
jsonResult = json.dumps(body)
server.send(bytes(str(jsonResult), "utf-8"))


buffer = server.recv(1024)
buffer = buffer.decode("utf-8")
