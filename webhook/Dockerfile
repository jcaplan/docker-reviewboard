FROM python:2-alpine

WORKDIR /webhook

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ./webhook.py
