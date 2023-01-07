FROM python:3.11.1-bullseye

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 9191
ENTRYPOINT ["python", "ip-exporter.py", "--port", "9191"]
