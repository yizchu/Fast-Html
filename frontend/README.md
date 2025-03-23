# Frontend of Fast-Html

## Environment
- Node.js >= 20.7.0
- npm >= 10.8.2

## Install Packages
```shell
npm install
```

## Run Dev
```shell
npm run dev
```
### Troubleshooting Electron Installation
```shell
npm install -g cnpm --registry=https://registry.npmmirror.com
cnpm install electron --save
```
## Build
### Build for Production
```shell
npm run build
```
### Build for Staging
```shell
npm run build:staging
```
## Preview
### Preview for Production
```shell
npm run preview
```
### Preview for Staging
```shell
npm run preview:staging
```
## .env Description

- This project exposes environment variables on `import.meta.env` object.
- Different modes (development/staging/production) correspond to different environment files (.env.*).
- .env file is always included, duplicate variables are overwritten by the specific mode file (.env.*).
