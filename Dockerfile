ARG PYTHON_VERSION=3.11-slim-bullseye

#base image
FROM python:${PYTHON_VERSION}

#prepare place to store project
ENV HomeForDocker /Users/kathe/workspace/learning_docker/
RUN mkdir -p $HomeForDocker
WORKDIR $HomeForDocker

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

#copy whole project to your docker home directory
COPY . $HomeForDocker

RUN pip install -r requirements.txt

EXPOSE 8000

#I don't have DB setup
# CMD python manage.py makemigrations
# CMD python manage.py migrate
CMD python manage.py runserver