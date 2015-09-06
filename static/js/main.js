Webcam.set({
        width: 600,
        height: 480,
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
}, 2000);
});
