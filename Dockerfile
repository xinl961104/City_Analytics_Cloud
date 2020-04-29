FROM alpine:latest

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

WORKDIR /app

COPY ./web_app /app

RUN pip3 install -r requirements.txt

EXPOSE 80

ENTRYPOINT [ "python3" ]
CMD ["web_app.py"]
