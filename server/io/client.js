const http       = require('http')
      server     = http.createServer(app),
      io         = require('socket.io')(http);

io.on('connection-client', function(socket){
	console.log('a user connected');
	socket.on('disconnect', function(){
		console.log('user disconnected');
	});
});

module.exports = io;