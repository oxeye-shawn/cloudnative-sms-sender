# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:latest

EXPOSE 8080

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt


WORKDIR /app
COPY . /app

CMD ["opentelemetry-instrument", "gunicorn", "--bind", "0.0.0.0:8080", "service:app"]

