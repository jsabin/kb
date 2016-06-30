import SimpleHTTPServer
import SocketServer
import logging
import threading
from BaseHTTPServer import BaseHTTPRequestHandler


class HttpServer:
    """
        Test HTTP server
    """

    def __init__(self, port):
        self.handler = ServerHandler
        SocketServer.TCPServer.allow_reuse_address = True  # Do not hold on to the port when done with resource
        self.httpd = SocketServer.TCPServer(("", port), self.handler)
        self.thread = threading.Thread(target=self.thread)
        self.thread.setDaemon(True)
        self.thread.start()

    def thread(self):
        self.httpd.serve_forever()

    def get_data(self):
        return self.handler.get_data()

    def set_data(self, data):
        return self.handler.set_data(data)

    def set_error(self, error_code):
        self.handler.set_error(error_code)

    def shutdown(self):
        self.httpd.shutdown()
        self.thread.join(timeout=3)
        logging.warning("=========== HTTP Server Shut Down ============")


# class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
class ServerHandler(BaseHTTPRequestHandler):
    data = None
    error = None

    def do_GET(self):
        # logging.warning(ServerHandler.data)
        if ServerHandler.error:
            self.send_error(ServerHandler.error)
        else:
            self.wfile.write(ServerHandler.data)

# noinspection PyPep8Naming
    def do_POST(self):
        ServerHandler.data = self.rfile.read(int(self.headers.getheader('Content-Length')))
        logging.warning(ServerHandler.data)
        self.send_response(200)

    @staticmethod
    def get_data():
        d = ServerHandler.data
        ServerHandler.data = None
        return d

    @staticmethod
    def set_data(data):
        ServerHandler.error = None
        ServerHandler.data = data

    @staticmethod
    def set_error(error_code):
        ServerHandler.error = error_code


if __name__ == '__main__':
    HttpServer(8999)
