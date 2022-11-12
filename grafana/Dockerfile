# Grafana latest docker image https://hub.docker.com/r/grafana/grafana-enterprise/tags
FROM grafana/grafana-enterprise:9.2.4-ubuntu

COPY grafana.ini /etc/grafana/grafana.ini

# Copy dashboards to lib folder
COPY dashboard-jsons/ /var/lib/grafana/dashboards
