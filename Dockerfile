ARG PYTHON_VERSION=3.11-slim-bullseye

#base image
FROM python:${PYTHON_VERSION}

#prepare place to store project
ENV APP_HOME /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#set work directory (where all upcoming commands will be applied)
WORKDIR $APP_HOME

#Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

#copy the project
COPY . .

EXPOSE 8000

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]