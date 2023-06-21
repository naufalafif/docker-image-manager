FROM node:18-buster as builder

# Set the working directory to /app inside the container
WORKDIR /app

# Copy app files
COPY ./apps/frontend .

# install packages
RUN yarn install

# Build the app
RUN yarn build

# Bundle static assets with nginx
FROM nginx:1.21.0-alpine as production

ENV NODE_ENV production

# Copy built assets from `builder` image
COPY --from=builder /app/dist /usr/share/nginx/html

# Add your nginx.conf
COPY ./apps/frontend/compose/prod/nginx.conf /etc/nginx/conf.d/default.conf

# Expose port
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]