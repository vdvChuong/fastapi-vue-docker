📖 Overview
This project consists of a FastAPI backend and a Vue.js frontend, containerized using Docker for easy development, testing, and deployment.

Backend (/backend)
Built with FastAPI, the backend provides a REST API that can handle requests, serve data, and optionally manage WebSocket connections.
It runs using Uvicorn on port 8000.

Frontend (/frontend)
Built with Vue.js, the frontend offers a reactive and interactive user interface, communicating with the backend API.
It runs using the Vue development server on port 8080.

### Installation
1. Navigate to the FastAPI (BE) directory and install dependencies:
   Version: python:3.12
   ```
   cd backend
   install -r requirements.txt
   ```

2. Navigate to the Vue (FE) directory and install dependencies:
   Version: node:22
   ```
   cd frontend
   npm install
   ```

### Running the Applications

- To run the Fastapi application:
  ```
  cd backend
  uvicorn main:app --port 8000 --host 0.0.0.0 --reload
  ```

- To run the Vue application:
  ```
  cd frontend
  npm run serve
  ```

- To build vue application:
   ```
   cd frontend
   npm run build
   ```

```
   frontend/
├── Dockerfile                  # Dockerfile for building and running the Vue app
├── package.json                # Project metadata and dependencies
├── public/                     # Static assets served by the Vue app
├── src/                        # Source code for the Vue app
│   ├── components/             # Vue components
│   │   └── HelloWorld.vue      # Example Vue component
├── dist/                       # (Generated after build) 
```

# Build the FastAPI backend image
   ```
docker build -t fastapi-backend ./backend
   ```

# Run the FastAPI container on port 8000
   ```
docker run -p 8000:8000 fastapi-backend
   ```

# Build the Vue frontend image using its Dockerfile
   ```
docker build -t my-vue-app -f frontend/Dockerfile .
   ```

# Run the Vue container on port 8080
   ```
docker run -p 8080:8080 my-vue-app
   ```
