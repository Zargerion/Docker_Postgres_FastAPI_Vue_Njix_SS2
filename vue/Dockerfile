FROM node:lts-alpine

ENV PATH /app/node_modules/.bin:$PATH
RUN npm install @vue/cli -g

ARG DIR=/vue
RUN mkdir -p ${DIR}
COPY ./vue ${DIR}
WORKDIR ${DIR}

RUN ls
RUN ls
RUN ls


RUN npm install

CMD ["npm", "run", "serve"]