FROM node:18-alpine
# Set the working directory to /app inside the container
WORKDIR /app
# Copy app files
# COPY package.json .
# COPY yarn.lock .
# # install packages
# RUN yarn install

# APP & node modules will be added by volumes

# Expose port
EXPOSE 3000
# Start nginx
CMD ["yarn", "dev"]