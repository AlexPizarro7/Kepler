FROM node:18.18.1

WORKDIR /kepler

COPY . .

RUN npm install

EXPOSE 4173

RUN npm run build

CMD ["npm","run","preview"]