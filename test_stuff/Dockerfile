FROM node:20
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm install pinia-plugin-persistedstate

EXPOSE 5173
CMD ["npm", "run", "dev"]
