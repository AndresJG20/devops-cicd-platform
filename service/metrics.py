from threading import Lock
from collections import Counter

class Metrics:
    def __init__(self):
        self.lock = Lock()
        self.requests = Counter()
        self.duration = Counter()

    def observe(self, route, status, seconds):
        with self.lock:
            self.requests[(route,status)] += 1
            self.duration[route] += seconds

    def render(self):
        with self.lock:
            lines = ["# TYPE http_requests_total counter"]
            for (route,status),value in sorted(self.requests.items()):
                lines.append(f'http_requests_total{{route="{route}",status="{status}"}} {value}')
            lines.append("# TYPE http_request_duration_seconds_sum counter")
            for route,value in sorted(self.duration.items()):
                lines.append(f'http_request_duration_seconds_sum{{route="{route}"}} {value:.6f}')
            return "\n".join(lines)+"\n"
