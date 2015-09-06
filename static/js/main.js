
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

