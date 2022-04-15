
let colorChange = document.querySelector('header');

let clickEvent = document.querySelector('DIV#red_header');
clickEvent.onclick = function(){
    colorChange.classList.add('red');
};

