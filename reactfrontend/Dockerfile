# Use official Node.js image for building
FROM node:20-alpine AS builder

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json first (leverage Docker cache)
COPY reactfrontend/package.json reactfrontend/package-lock.json ./

# Install only production dependencies
RUN npm install --omit=dev

# Copy the rest of the application files
COPY . .

# Build the React app
RUN npm run build

# Use a lightweight Nginx image for serving the built React app
FROM nginx:alpine

# Copy built React files to Nginx's default public folder
COPY --from=builder /app/build /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
