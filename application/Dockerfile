# Dockerfile
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements and source code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

# Expose the application port
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]

