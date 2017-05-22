<img src="logo pic link">

# ProtoNews

### Introduction

ProtoNews is a news recommendation application. Its primitive idea is to deliver top line news faster yet simpler. It runs machine learning modeling to perform intelligent news recommendations based on users' taps. ProtoNews makes reading news much easier and frees us from the pain of picking up a news article in a way that it just like already knows what we are expecting.  

[![Build Status]()]()
[![coverage-0%]()]()

<img src="a screenshot of website">

### Features

- F1
- F2
- F3
- F4

### Get Started

1. Run your mongodb server locally(download mongodb).
```sh
./mongod
```
2. We need to start the data generator, run news_deduper, news_fecther and news_monitor. 
```sh
./news_pipeline_launcher.sh
```

3. Run service.py, recommendation_service.py, server.py, click_log_processor.py to start all services.

4. Go to webserver/server 
`npm install`
`npm start` 
to start server 
5. Go to webserver/client 
 `npm run build` to create build folder 
then `npm start`. Later, it will jump to the login page, sign up first and log in. As so far, we are done!

### Architecture

- [Datapipe](#)
- [Backend](#)
- [Frontend](#)
- [Cloud-AWS](#)
