# Use a small pre-built image with nginx already installed
FROM nginx:alpine

# Copy our HTML file into the location nginx looks for website files
COPY app/index.html /usr/share/nginx/html/index.html

# Tell Docker that this container will use port 80 (standard web port)
EXPOSE 80

# Start nginx and keep it running (so the website is live)
CMD ["nginx", "-g", "daemon off;"]