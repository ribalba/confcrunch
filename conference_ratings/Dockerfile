# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=conference_ratings.settings
ENV SECRET_KEY=your-secret-key

# Set work directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port 8000
EXPOSE 8000

# Run the application
CMD ["gunicorn", "conference_ratings.wsgi:application", "--bind", "0.0.0.0:8000"]
