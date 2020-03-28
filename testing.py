from http.server import BaseHTTPRequestHandler, HTTPServer


class MyHeader(BaseHTTPRequestHandler):
    """ Этот класс используется для обработки HTTP-запросов, поступающих на сервер.
    Сам по себе он не может отвечать на любые реальные HTTP-запросы; он должен быть разделен на
    подклассы для обработки каждого метода запроса (например, GET или POST).
    BaseHTTPRequestHandlerпредоставляет ряд переменных класса и экземпляра,
    а также методы для использования подклассами.
    """
    def do_GET(self):
        """ Метод """
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
