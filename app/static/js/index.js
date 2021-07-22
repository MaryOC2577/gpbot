
// --   FUNCTION DEFINITION  --

document.getElementById("submitBtn").addEventListener("click", function (event) {
    event.preventDefault();
    event.stopPropagation();
    const $textInput = document.getElementById("text");
    const userText = $textInput.value;

    console.log("onSubmit called !!");

    const params = {
        method: "POST",
        headers: new Headers({ "content-type": "application/json" }),
        body: JSON.stringify({ text: userText }),
    };

    const fetchPromise = fetch("/find_place", params);
    fetchPromise.then(onServerResponse);

    //map
    // Initialize the platform object:
    var platform = new H.service.Platform({
        'apikey': '{nA_2GT2YF3clqlab3lCR8BNVlyVeSdcnmZ2Co_6d9VE}'
    });

    // Obtain the default map types from the platform object
    var maptypes = platform.createDefaultLayers();

    // Instantiate (and display) a map object:
    var map = new H.Map(
        document.getElementById('mapContainer'),
        maptypes.vector.normal.map,
        {
            zoom: 10,
            center: { lng: response.place_lng, lat: response.place_lat }
        });


});

function onServerResponse(response) {
    const JsonPromise = response.json();
    JsonPromise.then(onJson);
}

function onJson(response) {
    console.log(response);
    document.getElementById("chatzone").innerText = response.cleaned_text;
}



// --   CLIENT CODE DEFINITION  --

document.getElementById("chatbox").addEventListener("submit", onSubmit);
