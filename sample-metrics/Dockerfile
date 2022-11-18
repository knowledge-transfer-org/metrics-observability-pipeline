FROM python:3.9-slim as compiler
ENV PYTHONUNBUFFERED 1

LABEL Maintainer="guptaachin"

WORKDIR /app/

RUN python -m venv /opt/venv
# Enable venv
ENV PATH="/opt/venv/bin:$PATH"

COPY vir-env/requirements.txt /app/requirements.txt
RUN pip install -Ur requirements.txt

FROM python:3.9-slim as runner
WORKDIR /app/
COPY --from=compiler /opt/venv /opt/venv

# Enable venv
ENV PATH="/opt/venv/bin:$PATH"
COPY scripts/prometheus-metrics.py ./

# Needed for prometheus metrics generator to remove _created series
ENV PROMETHEUS_DISABLE_CREATED_SERIES=True

CMD ["./prometheus-metrics.py"] 
