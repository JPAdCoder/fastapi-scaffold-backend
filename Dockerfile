# Use the official Python 3.12 image as the base image
FROM python:3.12

# Set the timezone to Asia/Shanghai
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

# Set the working directory inside the container
WORKDIR /code

RUN ls -l

# Install dependencies
RUN pip install -r requirements.txt -i https://pypi.douban.com/simple

# Copy the rest of the application code into the container
COPY . /code/

# Specify the default command to run on container start
CMD ["python3", "main.py"]