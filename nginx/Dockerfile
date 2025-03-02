FROM nginx:latest

# Install OpenSSL for self-signed SSL certificate
RUN apt-get update && apt-get install -y openssl && rm -rf /var/lib/apt/lists/*

# Create directory for SSL certificates
RUN mkdir -p /etc/nginx/certs

# Generate self-signed certificate if it doesn't exist
RUN if [ ! -f /etc/nginx/certs/self-signed.crt ]; then \
        openssl req -x509 -newkey rsa:4096 -keyout /etc/nginx/certs/self-signed.key \
        -out /etc/nginx/certs/self-signed.crt -days 365 -nodes \
        -subj "/CN=localhost"; \
    fi

# Copy Nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose ports
EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
