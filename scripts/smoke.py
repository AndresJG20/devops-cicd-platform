import json
import sys
import time
import urllib.request

base = sys.argv[1] if len(sys.argv)>1 else "http://127.0.0.1:8080"
for attempt in range(30):
    try:
        with urllib.request.urlopen(base+"/health",timeout=2) as response:
            assert json.load(response)["status"]=="ok"
        with urllib.request.urlopen(base+"/ready",timeout=2) as response:
            assert json.load(response)["status"]=="ready"
        print("Smoke checks passed")
        break
    except Exception:
        if attempt==29:
            raise
        time.sleep(1)
