FROM python:3.10-slim

# Install build dependencies for compiling uWSGI and other packages with C extensions
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=storefront.settings
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app/

RUN python manage.py collectstatic --noinput
RUN python manage.py shell < dummydata.py


EXPOSE 8000

CMD ["uwsgi", "--http", "0.0.0.0:8000", "--module", "storefront.wsgi:application", "--master", "--processes", "4", "--threads", "2"]
