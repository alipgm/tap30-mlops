FROM python:3.12.6-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade pip --timeout=300 -i https://mirror-pypi.runflare.com/simple
RUN pip install --no-cache-dir -e . --timeout=300 -i https://mirror-pypi.runflare.com/simple

RUN python pipeline/run.py

EXPOSE 8080

CMD ["python", "web/application.py"]