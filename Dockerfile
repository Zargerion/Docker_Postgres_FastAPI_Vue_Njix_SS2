FROM alpine:latest
RUN apk update \
    && apk update
RUN apk add python3.10.6
COPY . .
RUN python3 setup.py

