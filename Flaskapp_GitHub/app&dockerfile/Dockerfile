FROM alpine:3.7

RUN apk add --no-cache python3 \
    && pip3 install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt                                                                            

EXPOSE 5000


CMD ["python3", "app.py"]