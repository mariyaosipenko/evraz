FROM node:16

ENV PORT 3000

WORKDIR /app
COPY package.json ./
COPY . .

EXPOSE ${PORT}

CMD yarn && yarn start