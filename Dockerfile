FROM python:3.7-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY .  /app/

RUN yum install -y libcurl make gcc autoconf && \
    run_install.sh && \
    yum clean all &&
    rm *.not_required *.log && pip install -r requirements.txt
# RUN pip install -r requirements.txt

