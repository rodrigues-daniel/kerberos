FROM ubuntu:16.04
MAINTAINER Daniel Rodrigues


RUN apt-get update
RUN apt-get install -y apt-utils apt-transport-https  debconf-utils  curl unixodbc-dev python3  python3-pip


RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql mssql-tools
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
RUN /bin/bash -c "source ~/.bashrc"


RUN apt-get -y install locales
RUN locale-gen en_US.UTF-8
RUN update-locale LANG=en_US.UTF-8

#RUN ["apt-get", "install","-y","unixodbc-dev"]
 

ENV PYTHONUNBUFFERED 1
RUN mkdir /config
ADD /config/requirements.pip /config
RUN pip3 install -r /config/requirements.pip
RUN mkdir /src;
WORKDIR /src