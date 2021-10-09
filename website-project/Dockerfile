FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /website

ADD . /website/

# Install requirements
COPY ./requirements.txt /website/requirements.txt

RUN pip install -r requirements.txt

COPY . /website/

