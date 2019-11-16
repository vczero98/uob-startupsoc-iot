var leds = [false, false, false, false, false, false];

$(document).ready(function() {
    $(".led").click(function() {
        if (leds[$(this).data("id")]) {
            $(this).removeClass("on");
        } else {
            $(this).addClass("on");
        }
        leds[$(this).data("id")] = !leds[$(this).data("id")];
        console.log(leds);
    });
});