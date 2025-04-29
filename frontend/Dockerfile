# Use Node 22 official image
FROM node:22

# Set working directory inside container
WORKDIR /app

# Copy frontend code into container
COPY ./frontend/ .

# Install npm dependencies
RUN npm install

# Expose the default Vue dev server port
EXPOSE 8080

# Start the Vue development server
CMD ["npm", "run", "serve"]
