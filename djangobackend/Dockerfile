# Use the official Python image as a base
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY req.txt .
RUN pip install --no-cache-dir -r req.txt

# Copy the rest of the Django project files
COPY . .

# Expose the port Django runs on
EXPOSE 8000

# Run migrations before starting the server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
