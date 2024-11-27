# # Use the official Python image
# FROM python:3.10-slim

# # Set the working directory inside the container
# WORKDIR /app

# # Copy the requirements file from the root directory
# COPY requirements.txt ./

# # Install dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the entire `app` directory into the container
# COPY app ./app

# # Copy other project files (e.g., database, tests, etc.)
# COPY . .

# # Set PYTHONPATH to include the `/app` directory
# ENV PYTHONPATH=/app

# # Expose the port your app will run on
# EXPOSE 8000

# # Command to run the application
# CMD ["python", "app/main.py"]
