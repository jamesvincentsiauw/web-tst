from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import http.client


def get():
    conn = http.client.HTTPSConnection("api.rajaongkir.com")
    headers = { 'key': "8673346f00df697bd0b951de5f847598" }
    conn.request("GET", "/starter/city", headers=headers)

    res = conn.getresponse()
    data = res.read()
    return data


class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        if self.path == "/getcity":
            res = json.loads(get())
            ret = []
            for row in res['rajaongkir']['results']:
                data = {
                    'city_id': row['city_id'],
                    'city_name': row['city_name']
                }
                ret.append(data)
            self.wfile.write(bytes(json.dumps(ret).encode('UTF-8')))
            return
        else:
            self.wfile.write(bytes("HAI".encode('utf-8')))
            return


def run():
    port = 8000
    with HTTPServer(("", port), myHandler) as httpd:
        print("serving at port ", port)
        httpd.serve_forever()


if __name__ == "__main__":
    run()
