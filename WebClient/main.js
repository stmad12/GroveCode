$(document).ready(function() {
    var socketsServer = 'http://localhost:3000/';
    var socket = io.connect(socketServer);
    
    socket.on('echo', function(data) {
        console.log('socket echo = ' + JSON.stringify(data));
        $('#dht-display').text(data.temp + "C, " + data.humi + "%");
        $('#range-display').text(data.range);
    });
});

$(document).ready(function() {
    var socketsServer = 'http://localhost:3000/';
    var socket = io.connect(socketServer);
    
    socket.on('echo', function(data) {
        console.log('socket echo = ' + JSON.stringify(data));
        $('#dht-display').text(data.touch + "Test");
        $('#range-display').text(data.range);
    });
});