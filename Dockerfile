FROM python:3.6-slim

RUN pip install requests argparse

COPY entrypoint.py /

ENV ATTEMPTS=20

ENV SLEEP=1

ENV RABBITMQ_MANAGEMENT_PORT=15672

ENTRYPOINT ["entry.sh"]
