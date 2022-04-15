addEventListener("load", readyForRun);

function readyForRun() {
    fetch('https://fourtonfish.com/hellosalut/?lang=fr')
        .then(response => response.json())
        .then(data => {
            let toAddAPIText = document.querySelector('DIV#hello');

            let textNode = document.createTextNode(data.hello);

            toAddAPIText.appendChild(textNode);

        })
}