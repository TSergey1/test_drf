FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip3 install -r /app/requirements.txt --no-cache-dir
COPY . .

