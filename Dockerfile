# Use the official Python 3.12 image as the base image
FROM python:3.12-slim

# Set the timezone to Asia/Shanghai
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

COPY . /code

WORKDIR /code

# Install Poetry
RUN pip install poetry

# Install dependencies
RUN poetry install

# Specify the default command to run on container start
CMD ["python3", "main.py"]