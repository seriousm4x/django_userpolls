FROM python:3-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /opt/app
COPY polls_project/ .

RUN apk update && \
    apk --no-cache add gcc musl-dev python3-dev libffi-dev openssl-dev cargo postgresql-dev && \
    python -m pip install --upgrade pip && \
    pip --no-cache-dir install -r requirements.txt && \
    apk del gcc musl-dev python3-dev libffi-dev openssl-dev cargo && \
	rm -rf /var/cache/apk/* && \
	rm -rf /root/.cache && \
	rm -rf /root/.cargo