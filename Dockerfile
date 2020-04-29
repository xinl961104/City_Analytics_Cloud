FROM python:alpine3.7

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip
    
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT [ "python" ]
CMD [ "web_app.py" ]