$("#webcam").webcam({

    width: 600,
    height: 600,
    mode: "save",
    swffile: "/static/jscam_canvas_only.swf", // canvas only doesn't implement a jpeg encoder, so the file is much smaller

	onTick: function() {},
	onSave: function(data) {
		console.log('here5678');
	},
	onCapture: function() {
		console.log('here1234');
	    webcam.save("http://localhost:5000/");
	    console.log('here139412323')
	},
	debug: function() {},
	onLoad: function() {
	    window.setInterval(function(){
	        webcam.capture();
        }, 2000);
	},
});
