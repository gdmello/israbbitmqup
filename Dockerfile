FROM python:3.6-slim

RUN pip install requests argparse

COPY entrypoint.py /

ENTRYPOINT ["python", "entrypoint.py"]
