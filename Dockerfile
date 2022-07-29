# Tell Docker use the official python image
FROM python:3.9

# Setting an enviroment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory of the container
RUN mkdir /app
WORKDIR /app
COPY ./app /app

# Install requirements
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt
