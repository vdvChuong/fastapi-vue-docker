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
