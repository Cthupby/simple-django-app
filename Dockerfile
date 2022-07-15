# Tell Docker use the official python 3 image
FROM python:3

# Setting an enviroment variable
ENV PYTHONUNBUFFERED 1

# Set the working directory of the container
RUN mkdir /app
WORKDIR /app
COPY ./app /app

# Install requirements
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt
