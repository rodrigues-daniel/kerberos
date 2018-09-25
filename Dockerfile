FROM python:3.6-stretch
RUN ["apt-get", "update"]
RUN ["apt-get", "install","-y","unixodbc-dev"]
ENV PYTHONUNBUFFERED 1
RUN mkdir /config
ADD /config/requirements.pip /config
RUN pip install -r /config/requirements.pip
RUN mkdir /src;
WORKDIR /src