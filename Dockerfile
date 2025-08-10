# Use official Python image as base
FROM python:3.10-slim

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=storefront.settings
ENV PYTHONUNBUFFERED=1

# Set work directory inside the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . /app/

# Collect static files (optional, depends if you use static files)
RUN python manage.py collectstatic --noinput

# Expose port 8000
EXPOSE 8000

# Run the Django app
CMD ["gunicorn", "storefront.wsgi:application", "--bind", "0.0.0.0:8000"]

