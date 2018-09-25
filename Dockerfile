FROM python:3.6 # imagename : version
  ENV PYTHONUNBUFFERED 1
  RUN mkdir /config
  ADD /config/requirements.pip /config
  RUN pip install -r /config/requirments.pip
  RUN mkdir /src;
WORKDIR /src