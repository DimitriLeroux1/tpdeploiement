FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./app/app.py .

EXPOSE 8080

CMD ["python","-m","app"]