/**
 * @Author: Dukecat
 * @Date:   2017-05-02T23:27:10-04:00
 * @Last modified by:   Dukecat
 * @Last modified time: 2017-05-11T21:21:15-04:00
 */





var express = require('express');
var rpc_client = require('../rpc_client/rpc_client');
var router = express.Router();

 /* GET news list. */
router.get('/userId/:userId/pageNum/:pageNum', function(req, res, next) {
  console.log('Fetching news...');
  user_id = req.params['userId'];
  page_num = req.params['pageNum'];

  rpc_client.getNewsSummariesForUser(user_id, page_num, function(response) {
    res.json(response);
  });
});

/* POST news click event. */
router.post('/userId/:userId/newsId/:newsId', function(req,res, next) {
  console.log('Logging news click...');
  user_id = req.params['userId'];
  news_id = req.params['newsId'];
  console.log(news_id);
  rpc_client.logNewsClickForUser(user_id, news_id);
  res.status(200);
});

module.exports = router;
