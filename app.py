from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        version = os.getenv("APP_VERSION", "v1.0")
        response = f"<h1>GitOps Pipeline Active!</h1><p>Running Version: <b>{version}</b></p>"
        self.wfile.write(response.encode('utf-8'))

if __name__ == '__main__':
    port = 8080
    print(f"Server starting on port {port}...")
    server = HTTPServer(('0.0.0.0', port), SimpleHandler)
    server.serve_forever()
