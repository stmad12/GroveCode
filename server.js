var http = require('http');
var socketio = require('socket.io');
var bodyParser = require('body-parser');
var express = require('express');

var app = express();
var server = http.createServer(app);
var io = socketio(server);

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false}));

app.get('/', function (req, res) {
  res.send('Hello World!');
});

app.post('/', function(req,res) {
    console.log('post / =' + JSON.stringify(req.body));
    io.sockets.emit('echo', req.body);
    res.status(200).send('got it');
});

server.listen(3000, function () {
  console.log('Example app listening on port 3000!')
});