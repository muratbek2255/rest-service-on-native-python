from datetime import date, datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

import environs

env = environs.Env()

IP = env('HOST')
PORT = int(env('PORT'))


class NeuralHTTP(BaseHTTPRequestHandler):

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        decode_body = post_body.decode()
        json_body = json.loads(decode_body)
        self.wfile.write(bytes('{"message": "Success"}', "utf-8"))

        now_date = str(datetime.now().strftime('%H:%M %d.%m.%y'))
        print(now_date)

        if now_date == json_body['time']:
            print("#Running name")
            print(json_body['name'])


server = HTTPServer((IP, PORT), NeuralHTTP)
print('Server is running...')

server.serve_forever()
server.server_close()
print('Server was stoped!')
