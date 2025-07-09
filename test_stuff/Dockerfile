FROM node:20
WORKDIR /app
COPY . .
RUN npm install
RUN npm install pinia-plugin-persistedstate
RUN npm run build
# Serve with a simple static server (e.g., serve)
RUN npm install -g serve
EXPOSE 5173
CMD ["serve", "-s", "dist", "-l", "5173"]