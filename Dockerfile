FROM python:3.7.2-alpine3.8


COPY tests /src/tests
COPY requirements.txt /src/
WORKDIR /src

RUN pip install -r /src/requirements.txt
