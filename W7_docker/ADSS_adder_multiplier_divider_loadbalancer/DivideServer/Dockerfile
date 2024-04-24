FROM node:16

WORKDIR /usr/src/app
COPY src/app.js .
RUN npm install express ejs
EXPOSE 8080
CMD ["node", "app.js"]
