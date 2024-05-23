ARG PYTHON_VERSION=3.11-slim-bullseye

#base image
FROM python:${PYTHON_VERSION}

#prepare place to store project
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#set work directory (where all upcoming commands will be applied)
WORKDIR /code

#Copy requirements and install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

#copy the current directory . in the project to the workdir . in the image
COPY . /code/

EXPOSE 8000

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.1:8000"]