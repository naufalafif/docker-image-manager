FROM python:3.9.10-slim

ENV PYTHONUNBUFFERED 1

EXPOSE 8000
WORKDIR /app

COPY . .

RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat python3-pygments && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY poetry.lock pyproject.toml ./
RUN pip3 install poetry==1.4.0\ && \
    poetry config virtualenvs.in-project false && \
    poetry install

CMD poetry run gunicorn app.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
