
let toAddlist = document.querySelector('UL.my_list');

let clickEvent = document.querySelector('DIV#add_item');


clickEvent.onclick = () => {
    const newElement = document.createElement('li');

    const newTextElement = document.createTextNode('Item');

    newElement.appendChild(newTextElement);

    toAddlist.appendChild(newElement);
    
}