module.exports = io => {
    const pi = io.of("/pi")

    pi.on('connection', function(socket){
        console.log('Pi connected');
        socket.on('disconnect', function(){
            console.log('Pi disconnected');
        });
    });

    // io.on('connection', function (socket) {
    //     socket.emit('news', { hello: 'world' });
    //     socket.on('my other event', function (data) {
    //       console.log(data);
    //     });
    // });

    return io;
}