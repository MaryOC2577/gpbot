
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
    document.getElementById("chatzone").innerText = response.cleaned_text;
    document.getElementById("wikizone").innerText = response.wiki_info;
    $.ajax(displayMap(response.place_lat, response.place_lng));
}



// --   CLIENT CODE DEFINITION  --

document.getElementById("chatbox").addEventListener("submitBtn", onSubmit);
