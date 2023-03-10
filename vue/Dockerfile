FROM node:14-alpine

ARG DIR=/vue

RUN mkdir -p ${DIR}
COPY . ${DIR}
WORKDIR ${DIR}

RUN npm install -g npm
RUN npm install 

COPY ./package.json ${DIR}
COPY ./packege-lock.json ${DIR}

CMD ["npm", "run", "serve"]