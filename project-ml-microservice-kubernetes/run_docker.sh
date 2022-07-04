#!/usr/bin/env bash

# Step 1:
# Build image and add a descriptive tag
docker build --tag=udacityproj4 .

# Step 2:
# List docker images
docker image ls

# Step 3:
# Run flask app
# exposed container port (80): flask app port (5000)
docker run -p 8000:80 udacityproj4

# docker system prune -a