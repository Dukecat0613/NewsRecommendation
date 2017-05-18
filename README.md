# NewsRecommendation
The project is to build a recommendation system based on user behaviors. We used Kafka as message queue, Pyjsonrpc as RPC(Remote Procedure Call), mongodb as NoSQL database, tensorflow as machine learning framework, React as frontend framework and node.js as backend server to achieve the recommendation system.

## How to run?
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
