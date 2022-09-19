FROM nginx:1.23.1-alpine

RUN apk update
RUN apk add vim

COPY ./config/nginx.conf /etc/nginx/nginx.conf
