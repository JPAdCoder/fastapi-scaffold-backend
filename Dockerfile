# Use the official Python 3.12 image as the base image
FROM python:3.12

# Set the timezone to Asia/Shanghai
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

# Set the working directory inside the container
WORKDIR /code

# Copy the poetry files (pyproject.toml and poetry.lock) into the container
COPY pyproject.toml poetry.lock /code/

# Install poetry
RUN pip install poetry

# Install project dependencies using poetry
RUN poetry install

# Copy the rest of the application code into the container
COPY . /code/

# Specify the default command to run on container start
CMD ["poetry", "run", "python3", "main.py"]