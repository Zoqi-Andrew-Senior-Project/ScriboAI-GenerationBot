# nginx/Dockerfile
FROM nginx:alpine

# Copy custom Nginx configuration file
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy frontend build files (if you have a frontend)
COPY ../frontend/build /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
