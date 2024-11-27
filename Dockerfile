# Use the official Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements files to the container
COPY requirements.txt app/requirements.txt ./

# Install dependencies from both requirements files
RUN pip install -r requirements.txt

# Copy all project files to the container
COPY . .

# Expose the port your app will run on (assume port 8000)
EXPOSE 8000

# Command to run the application (adjust based on your entry point)
CMD ["python", "app/main.py"]
