var leds = [false, false, false, false, false, false];

const socket = io('/client');

socket.on('flame-on', function (data) {
    console.log('flame on');
    $('#flame').addClass('on');
});

socket.on('flame-off', function (data) {
    console.log('flame off');
    $('#flame').removeClass('on');
});

$(document).ready(function() {
    $(".led").click(function() {
        console.log("clicked LED");
        if (leds[$(this).data("id")]) {
            $(this).removeClass("on");
        } else {
            $(this).addClass("on");
        }
        leds[$(this).data("id")] = !leds[$(this).data("id")];
        console.log(leds);
    });

    $('#submit').click(function() {
        console.log("clicked Go!");
        socket.emit('led-state', { state: leds });
    });
});
