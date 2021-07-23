FROM python:3.8

RUN mkdir -p /code/
COPY serdis_server /code/serdis_server
COPY requirements.txt /code/
WORKDIR /code
RUN pip install --no-cache-dir -r requirements.txt