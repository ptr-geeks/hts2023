FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r /app/requirements.txt

COPY server /app

USER 1001:1001

# --cap-add CAP_NET_BIND_SERVICE
EXPOSE 80
ENTRYPOINT gunicorn -c python:config -w 32 -b 0.0.0.0:80 server:app
