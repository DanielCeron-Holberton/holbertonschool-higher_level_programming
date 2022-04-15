

let urlToRequest = fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => response.json())
    .then(data => {
        let toAddAPIText = document.querySelector('DIV#character');
        let charactherName = data.name;
        let charactherNode = document.createTextNode(charactherName);
        
        toAddAPIText.appendChild(charactherNode);
    });

