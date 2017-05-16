# NewsRecommendation
The project is to build a recommendation system based on user behaviors. We used RabbitMQ as message queue, Pyjsonrpc as rpc, mongodb as database, tensorflow as machine learning framework, React as front end framework and node.js as backend server to achieve the recommendation system.

## How to run?
Firstly, we need to start the data generator, run news_deduper, news_fecther and news_monitor. One thing needs to mention is that you have to use your own RabbitMQ queue url and name, you have to go to https://www.cloudamqp.com/ to create three queues, LOG_CLICKS_TASK_QUEUE, DEDUPE_NEWS_TASK_QUEUE, SCRAPE_NEWS_TASK_QUEUE. The second is you have to go to https://newsapi.org/ to create your own API key. Third, run your mongodb server locally(Just download mongodb and run `./mongod`). After creating and replacing the code, run data generator mentioned before. 

Then run service.py, recommendation_service.py, server.py, click_log_processor.py to start all services.

Finally, go to webserver/server `npm install` and `npm start` to start server and webserver/client `npm run build` to create build folder then `npm start`. Later, it will jump to the login page, sign up first and log in. As so far, we are done!
