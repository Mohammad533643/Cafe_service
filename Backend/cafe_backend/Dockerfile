FROM python:3.13.5

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV PIP_INDEX_URL=https://mirrors.aliyun.com/pypi/simple/
ENV PIP_TRUSTED_HOST=mirrors.aliyun.com
ENV PIP_DEFAULT_TIMEOUT=200
ENV PIP_RETRIES=10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir \
    --default-timeout=200 \
    --retries=10 \
    --disable-pip-version-check \
    -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]