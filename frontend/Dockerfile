# FROM ubuntu:latest
# LABEL authors="lysedorzea"

# ENTRYPOINT ["top", "-b"]

FROM node:18

# Dossier de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY package*.json ./

# Installer les dépendances
RUN npm install

# Copier le reste du projet
COPY . .

# Exposer le port Vite/SvelteKit
EXPOSE 5173

# Lancer SvelteKit en mode dev, accessible depuis l'extérieur
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "5173"]



#
## -----------------------------
## 1. Build stage
## -----------------------------
#FROM node:18 AS builder
#
## Create app directory
#WORKDIR /app
#
## Copy package files
#COPY package*.json ./
#
## Install dependencies
#RUN npm install
#
## Copy the rest of the project
#COPY . .
#
## Build the SvelteKit project
#RUN npm run build
#
#
## -----------------------------
## 2. Production stage
## -----------------------------
#FROM node:18 AS runner
#
#WORKDIR /app
#
## Copy built files from builder
#COPY --from=builder /app/build ./build
#COPY package*.json ./
#
## Install only production dependencies
#RUN npm install --omit=dev
#
## Expose the port used by SvelteKit
#EXPOSE 5173
#
## Disable telemetry
#ENV NODE_ENV=production
#
## Start the server
#CMD ["node", "build"]
