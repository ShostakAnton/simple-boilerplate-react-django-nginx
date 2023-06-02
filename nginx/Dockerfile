FROM node:20-alpine as build

WORKDIR /app

COPY /client .

RUN npm install

RUN npm run build

FROM nginx:latest

COPY --from=build /app/build /usr/share/nginx/html
