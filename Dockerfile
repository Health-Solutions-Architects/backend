FROM python:3.11-alpine as ws-api

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV PYTHONPATH=$PYTHONPATH:/app

EXPOSE 6000

CMD ["uvicorn", "src.api.app:app", "--no-server-header", "--workers", "2", "--host", "0.0.0.0", "--port", "5000"]
