
#Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to /app
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5000

# Define environment variable for Flask
ENV FLASK_APP=run.py

# Run the application
CMD ["python", "run.py"]