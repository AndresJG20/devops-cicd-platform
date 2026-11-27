import unittest, threading, urllib.request, urllib.error, json
from http.server import ThreadingHTTPServer
from service import Handler

class ServiceTests(unittest.TestCase):
    def test_routes(self):
        server=ThreadingHTTPServer(("127.0.0.1",0),Handler)
        t=threading.Thread(target=server.serve_forever,daemon=True)
        t.start()
        base="http://127.0.0.1:"+str(server.server_port)
        try:
            with urllib.request.urlopen(base+"/health") as r:
                self.assertEqual(json.load(r),{"status":"ok"})
            with self.assertRaises(urllib.error.HTTPError) as e:
                urllib.request.urlopen(base+"/missing")
            self.assertEqual(e.exception.code,404)
        finally:
            server.shutdown()
            server.server_close()
            t.join()
