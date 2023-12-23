FROM python:3.11.1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY app /app

EXPOSE 5002

CMD ["python", "app/app.py"]