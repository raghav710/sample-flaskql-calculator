FROM python:3.11-slim-buster

# Install dependencies
WORKDIR /app
RUN pip install Flask pytest

# Expose port for the Flask application
EXPOSE 5000

# Define the command to run the application
CMD ["python", "app.py"]