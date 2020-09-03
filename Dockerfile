FROM ubuntu:bionic

USER root

RUN apt-get update
RUN apt-get install -y python3-pip git

# install dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt 

# Copy app over
COPY app app/.
COPY run.py .
COPY config.py .
COPY database database/.
COPY migrations migrations/.

# make upload directory
RUN mkdir /uploads

# Setup flask
ENV username=dummy
ENV FLASK_ENV=production
ENV FLASK_APP=run.py
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# db wait helper
COPY wait-for-it.sh /usr/local/bin/

COPY bootstrap.sh /usr/local/bin/
ENTRYPOINT ["bash", "wait-for-it.sh", "db:5432", "--", "bash", "bootstrap.sh"]