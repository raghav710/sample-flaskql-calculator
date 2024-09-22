FROM python:3.11-slim-buster

# Copy application code
COPY . /app

# Install dependencies
WORKDIR /app
RUN pip install Flask

# Expose port for the Flask application
EXPOSE 5001

# Define the command to run the application
CMD ["python", "history.py"]