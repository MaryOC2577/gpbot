
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

});

function onServerResponse(response) {
    const JsonPromise = response.json();
    JsonPromise.then(onJson);
}

function onJson(response) {
    console.log(response);
    document.getElementById("chatzone").innerText += response.text + "\n GrandPy Bot a bien reçu votre demande.\n\n";
    document.getElementById("adress").innerText += response.coords.adress + "\n\n";
    document.getElementById("wikizone").innerText += response.wiki_info[0] + "\n\n";
    document.getElementById("wikiurl").innerHTML = "<a href='" + response.wiki_info[1] + "'>Consultez la page Wikipédia ici.</a>\n"
    if (response.text == "") {

    } else {
        displayMap(response.coords["coords"]["lat"], response.coords["coords"]["lng"]);
    }

}



function displayMap(lati, longi) {
    document.getElementById("mapContainer").innerText = ""
    // Initialize the platform object:
    var platform = new H.service.Platform({
        'apikey': "x",
        'app_id': 'x'

    });

    // Obtain the default map types from the platform object
    var maptypes = platform.createDefaultLayers();

    // Instantiate (and display) a map object:
    var map = new H.Map(
        document.getElementById('mapContainer'),
        maptypes.vector.normal.map,
        {
            zoom: 13,
            center: { lng: longi, lat: lati }
        });
    var locationMarker = new H.map.Marker({ lat: lati, lng: longi });
    map.addObject(locationMarker);
}