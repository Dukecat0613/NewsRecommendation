(logo pic link)

(Name Logo -- ProtoNews)

## Introduction

ProtoNews is a news recommendation application. Its primitive idea is to deliver top line news faster yet simpler. It runs machine learning modeling to perform intelligent news recommendations based on users' taps. ProtoNews makes reading news much easier and frees us from the pain of picking up a news article in a way that it just like already knows what we are expecting.  

(a screenshot of website)

## Features

- F1
- F2
- F3
- F4

## Get Started

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

## Architecture

- [Data Pipeline](#data-pipeline)
  - [Kafka](#kafka)
  - [MongoDB](#mongodb)
  - [Redis](#redis)
- [Back-End](#back-end)
  - [Express](#express)
  - [Node.js](#nodejs)
- [Front-End](#front-end)
- [Cloud-AWS](#cloud-aws)
  - [Database](#database)
  - [Kafka Cluster](#kafka-cluster)
  - [Web Server](#web-server)

---------

**<a name="data-pipeline"></a>Data Pipeline**

(A pic for our data pipeline)

  - <a name="kafka"></a>Kafka - Data Transportation

  - <a name="mongodb"></a>MongoDB

  - <a name="redis"></a>Redis

**<a name="back-end"></a>Back-End**

Node.js + Express as Back-End framework.

  - <a name="express"></a>Express

  - <a name="nodejs"></a>Node.js

**<a name="front-end"></a>Front-End**

React as Front-End framework

**<a name="cloud-aws"></a>Cloud-AWS**

We deployed our Web App on AWS EC2 instances.

 <a name="database"></a>Database

  * MongoDB

  * Redis

 <a name="kafka-cluster"></a>Kafka Cluster

  *

  *

 <a name="web-server"></a>Web Server
	
  * Server

  * Client

## Team

[![Hang Wu](https://avatars2.githubusercontent.com/u/23732977?v=3&s=400 = 200x200)](https://github.com/Dukecat0613) | [![Yuxiang Wang](https://avatars3.githubusercontent.com/u/18521999?v=3&u=efb9e4252e5dd007610874e1e67a4026efbd9644&s=400 = 200x200)](https://github.com/kuroega)
---|---
[Hang Wu](https://github.com/Dukecat0613) |[Yuxiang Wang](https://github.com/kuroega)

## License
