
# docker build --target backend --no-cache -t tecinforibeiro/health_solutions_architects:backend .
FROM python:3.10 as backend

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV PYTHONPATH=$PYTHONPATH:/app

EXPOSE 6000

CMD ["uvicorn", "src.app:app", "--no-server-header", "--host", "0.0.0.0", "--port", "5000"]
