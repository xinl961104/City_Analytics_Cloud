FROM alpine:latest

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

WORKDIR /app

COPY ./Tweets /app

RUN pip3 install tweepy

ENTRYPOINT [ "python3" ]
CMD ["stream_listener.py"]