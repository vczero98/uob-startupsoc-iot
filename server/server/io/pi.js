module.exports = (io, deviceState) => {
    const pi = io.of("/pi")

    pi.on('connection', socket => {
        console.log('Pi connected');
        socket.on('disconnect', () => {
            console.log('Pi disconnected');
        });

        socket.on('flame_state', data => {
            if (data.secret && (data.secret == process.env.PI_SECRET)) {
                console.log('received ' + data.state);
                deviceState.flame = data.state;
                deviceState.handleFlameUpdated()
            }
        });

        deviceState.handleLightsUpdated = () => {
            pi.emit('led_state', deviceState.lights);
            console.log("State emitted to Pi");
        }
    });

    return io;
}