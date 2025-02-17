# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file
COPY djangobackend/requirements.txt ./

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django app to the container
COPY . .

# Expose port 8000 to be accessible from outside the container
EXPOSE 8000

# Set the command to run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
