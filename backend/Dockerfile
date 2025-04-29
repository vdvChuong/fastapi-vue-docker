# Use a base Python image
FROM python:3.12

# Set working directory inside the container
WORKDIR /app/backend

# Copy the backend directory contents into the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port FastAPI will run on
EXPOSE 8000

# Run the FastAPI app with uvicorn (in reload mode for development)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
