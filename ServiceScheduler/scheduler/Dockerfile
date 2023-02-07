FROM python:3-slim

WORKDIR /app

RUN pip3 install pika && \
    pip3 install flask && \
    pip3 install requests && \
    pip3 install mysql-connector-python && \
    pip3 install redis

COPY . /app
COPY entrypoint.sh /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
