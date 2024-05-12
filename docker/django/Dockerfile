FROM python:3.10.0-slim-buster

ENV APP_HOME = /app 
RUN mkdir ${APP_HOME}  

# RUN mkdir ${APP_HOME}/staticfiles 
WORKDIR ${APP_HOME}


LABEL maintainer="emmanuelthedeveloper@gmail.com"
LABEL name="Emmanuel Langat"

ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get install -y libpq-dev \
    && apt-get install -y gettext \
    && apt-get -y install netcat gcc postgresql \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip 

COPY ./requirements.txt   /app/requirements.txt

RUN pip3 install -r /app/requirements.txt


COPY . .
COPY . ${APP_HOME}

COPY ./docker/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

EXPOSE 8000


# RUN python3 manage.py migrate --no-input
# RUN python3 manage.py collectstatic --no-input
# CMD [ "python3", "manage.py" , "runserver" ]