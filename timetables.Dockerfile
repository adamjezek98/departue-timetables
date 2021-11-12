FROM python:3.8
WORKDIR /app/src
COPY . /app
RUN set -e && pip install --upgrade pip pipenv
RUN set -e && pipenv install --system --deploy --ignore-pipfile
#RUN set -e && python timetables/manage.py makemigrations

