FROM alpine
RUN apk add --no-cache python3
WORKDIR /usr/src/app
COPY Data.txt ./data.txt
COPY app.py ./
CMD [ "python3", "./app.py" ]
