Webcam.set({
        width: 320,
        height: 240,
        flip_horiz: true,
    });
Webcam.attach( '#my_camera' );

function take_snapshot() {
    Webcam.snap( function(data_uri) {
        // snap complete, image data is in 'data_uri'
        Webcam.upload( data_uri, '/image_upload', function(code, text) {
            // Upload complete!
            // 'code' will be the HTTP response code from the server, e.g. 200
            // 'text' will be the raw response content
            console.log(text);
        } );

    });
}
Webcam.on("live", function() {

window.setInterval(function(){
    take_snapshot();
}, 1000);
});

function scrollBottom(){
    $("html, body").animate({ scrollTop: $(document).height() }, "fast");
}

function appendLine(text) {
    $("#poetry").append(text + "<br>");
}

// send request to server
// get back a line of poetry
function poll() {
    setTimeout(function() {
        $.ajax({
            url: "/poem",
            type: "GET",
            success: function(data) {
                appendLine(data);
                scrollBottom();
            },
            complete: poll,
            timeout: 2000
        })
    }, 2000);
};

poll();

