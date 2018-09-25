FROM python:3.6-stretch

ENV ACCEPT_EULA Y
RUN ["curl" ,"https://packages.microsoft.com/keys/microsoft.asc" ,"|", "apt-key", "add" ,"-"]
RUN ["curl" ,"https://packages.microsoft.com/config/debian/9/prod.list", ">", "/etc/apt/sources.list.d/mssql-release.list"]
RUN ["apt-get", "update"]
RUN ["apt-get", "install","-y","unixodbc-dev"]
RUN ["apt-get", "install","msodbcsql17"]
ENV PYTHONUNBUFFERED 1
RUN mkdir /config
ADD /config/requirements.pip /config
RUN pip install -r /config/requirements.pip
RUN mkdir /src;
WORKDIR /src