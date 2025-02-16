# Use official Node.js image with a smaller base
FROM node:20-alpine AS builder

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json first to leverage Docker cache
COPY package.json package-lock.json ./

# Install dependencies using npm ci (faster & more reliable than npm install)
RUN npm ci --only=production

# Copy the React project files
COPY . .

# Build the React app
RUN npm run build

# Use a lightweight Nginx image for serving the React app
FROM nginx:alpine

# Copy built React files to Nginx's default public folder
COPY --from=builder /app/build /usr/share/nginx/html

# Expose port 80 for serving the app
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
