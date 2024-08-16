# Use an official Python runtime as a parent image
FROM python:3.12.4

# Set the working directory in the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the project code into the container
COPY . .

# Expose the port your Django app listens on
EXPOSE 80

# Run the command to start your Django app
CMD ["python", "manage.py", "runserver", "[::]:80"]