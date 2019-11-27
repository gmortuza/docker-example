FROM python:latest

ENV VERSION 1.0

LABEL maintainer="golammortuzaabhi@gmail.com"

COPY main.py /

CMD [ "python", "./main.py" ]

COPY / test
