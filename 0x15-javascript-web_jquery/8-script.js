let urlToRequest = fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
        let toAddAPIText = document.querySelector('UL#list_movies');


        for (let index = 0; data.results[index]; index++) {
            const newList = document.createElement('li');
            let movieNode = document.createTextNode(data.results[index].title + ' \n');
            newList.appendChild(movieNode);
            toAddAPIText.appendChild(newList);
        }


    });
