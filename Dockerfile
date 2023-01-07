FROM python:3.11.1-bullseye

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "ip-exporter.py", "--port", "9191"]
EXPOSE 9191
