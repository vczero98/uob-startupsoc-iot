module.exports = (io, deviceState) => {
	const client = io.of("/client");

    client.on('connection', function(socket){
        console.log('Client connected');
        socket.on('disconnect', function(){
            console.log('Client disconnected');
		});
		
		deviceState.handleFlameUpdated = () => {
			console.log("emmitting " + deviceState.flame);
			client.emit(deviceState.flame ? 'flame-on' : 'flame-off');
		}
    });

    // io.on('connection', function (socket) {
    //     socket.emit('news', { hello: 'world' });
    //     socket.on('my other event', function (data) {
    //       console.log(data);
    //     });
    // });

    return io;
}