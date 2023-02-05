FROM python:3-slim

WORKDIR /app

RUN pip3 install pika && \
    pip3 install flask && \
    pip3 install requests && \
    pip3 install mysql-connector-python

COPY . /app

EXPOSE 5000

CMD [ "python3", "appointment.py" ]

