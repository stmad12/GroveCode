var Mongo = require('mongodb').MongoClient;
const MONGO_URL = 'mongodb://localhost:27017/iot';
var http = require('http');
var socketio = require('socket.io');
var bodyParser = require('body-parser');
var express = require('express');

Mongo.connect(MONGO_URL, function(err,db) {
    if(err) {
        // TODO handle error
    }
    Mongo.ops = {};
    
    Mongo.ops.find = function(collection, json,callback) {
        db.collection(collection).find(json).toArray(function(err,docs){if (callback) callback(arr,docs);
            });
    };



var app = express();
var server = http.createServer(app);
var io = socketio(server);

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false}));

app.get('/', function (req, res) {
  res.send('Hello World!');
});

app.post('/echo', function(req,res) {
    console.log('post / =' + JSON.stringify(req.body));
    io.sockets.emit('echo', req.body);
    res.status(200).send('got it');
});

server.listen(3000, function () {
  console.log('Example app listening on port 3000!')
});