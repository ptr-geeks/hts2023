import gunicorn
from prometheus_flask_exporter.multiprocess import GunicornPrometheusMetrics

gunicorn.SERVER = "Janezov Web Server 4.2.0"
gunicorn.SERVER_SOFTWARE = "Janezov Web Server 4.2.0"

def when_ready(server):
    GunicornPrometheusMetrics.start_http_server_when_ready(9090)

def child_exit(server, worker):
    GunicornPrometheusMetrics.mark_process_dead_on_child_exit(worker.pid)
