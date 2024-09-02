FROM alpine:latest
WORKDIR /app
COPY . /app

# Update package repositories and install any dependencies
RUN apk update && \
    apk add --no-cache <dependency1> <dependency2>

# Expose necessary ports
EXPOSE 80

# Define environment variables
ENV ENV_VAR_NAME=value

CMD ["command-to-start-app"]
