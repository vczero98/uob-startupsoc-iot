module.exports = (io, deviceState) => {
	const client = io.of("/client");

    client.on('connection', socket => {
        console.log('Client connected');
        socket.on('disconnect', () => {
            console.log('Client disconnected');
        });
        
        socket.on('led-state', state => {
            console.log("Received " + JSON.stringify(state));
            deviceState.lights = state;
            deviceState.handleLightsUpdated();
        });
		
		deviceState.handleFlameUpdated = () => {
			console.log("emitting " + deviceState.flame);
			client.emit(deviceState.flame ? 'flame-on' : 'flame-off');
		}
    });

    return io;
}