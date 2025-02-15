# Start with a lightweight Python image
FROM python:3.10-alpine

# Set working directory inside the container
WORKDIR /app

# Copy only the requirements file first (for efficient caching)
COPY requirements.txt .

# Install dependencies (avoid cache to reduce image size)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the application's port
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
