from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
    def do_time(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write(str("<b> Hello World !</b>"
                        + "<br><br>Current time: ").encode())

    def do_date(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(str('''
        Hello date World!!
        ''').encode())
        return
    
    def do_self(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(str('''
        Hello self World!!
        ''').encode())
        return

    def do_GET(self):
        if self.path == '/api/time':
            self.do_time()
        elif self.path == '/api/date':
            self.do_date()
        # elif self.path == '/api/':
        #     self.do_self()
        else:
            self.do_self()

# server = HTTPServer(('', port), handler)
# print('Started httpserver on port')

# #Wait forever for incoming http requests
# server.serve_forever()