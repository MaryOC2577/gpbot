
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
    document.getElementById("chatzone").innerText = response.text + "\n GrandPy Bot a bien reçu votre demande.\n";
    document.getElementById("adress").innerText = response.coords.adress;
    document.getElementById("wikizone").innerText = response.wiki_info;
    displayMap(response.coords["coords"]["lat"], response.coords["coords"]["lng"]);
}
