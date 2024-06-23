# Time:   ${time}
# Author: ${author}
# Email:  ${email}

FROM python:3.12-slim

# Set the timezone to Asia/Shanghai
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

COPY . /code

WORKDIR /code

# Install Poetry
RUN pip3 install poetry -i https://pypi.tuna.tsinghua.edu.cn/simple

# Install dependencies
RUN poetry install --no-root


# Specify the default command to run on container start
CMD ["poetry", "run", "python", "-m", "main"]