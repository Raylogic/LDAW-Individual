FROM python:3.7-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /app
EXPOSE 5000
COPY requirements*.txt ./
RUN pip install -r requirements.txt
COPY . .

CMD ["python", "ejemplo.py"]
