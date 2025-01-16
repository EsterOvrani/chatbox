# Use Python 3.12 as base image
FROM python:3.12-slim

# Set working directory in container
WORKDIR /app

# Copy only requirements file first
COPY requirements.txt .

# Install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy application code
COPY templates /app/templates
COPY chat_server.py .
COPY chats_massage /app/chats_massage

# Expose port 5000
EXPOSE 5000

# Entry point to run the application
CMD ["python3", "chat_server.py"]

