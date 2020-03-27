from http.server import BaseHTTPRequestHandler, HTTPServer


class MyHeader(BaseHTTPRequestHandler):

    def do_GET(self):

        print('Вы в GET request')
        self.send_response(200) #200 код - подключение успешно
        self.send_header('Content-type', 'text-plain')
        self.end_headers()

        self.wfile.write('<head><meta charset="utf-8" /></head>  '
                         '<h1 align="center">Hello!</h1>'
                         ' <p align="right">Привет Мир, сервер работает!</p>'.encode())

httpd = HTTPServer(('localhost', 8080), MyHeader)

print('Запуск...')
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print('Пока!')
