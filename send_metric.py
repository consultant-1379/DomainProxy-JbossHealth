import requests
import sys
# TYPE dpha_healthcheck gauge

def send_metric(job_name, metric_name, metric_value, ip_addr, hostname):
     response = requests.post('http://{i}:9091/metrics/job/{j}/hostname/{h}'.format(i=ip_addr, j=job_name, h=hostname), data='{k} {v}\n'.format(k=metric_name, v=metric_value).encode())
     return response.status_code,response.content;

send_metric(job_name=sys.argv[1], metric_name="dpha_healthcheck", metric_value=sys.argv[2], ip_addr=sys.argv[3], hostname=sys.argv[4])


