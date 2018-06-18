# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# so halt
RUN apt-get update && apt-get install -y \
python-mysqldb

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "-u", "futtie.py"]
