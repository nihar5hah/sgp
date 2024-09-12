# Use a lightweight Python image
FROM python:3.9-slim

# Install system dependencies required for numpy
RUN apt-get update && apt-get install -y \
    build-essential \
    libatlas-base-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . /app

# Upgrade pip and install dependencies
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

# Expose the required port
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
