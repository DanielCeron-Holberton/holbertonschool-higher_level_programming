let colorChange = document.querySelector('header');

let clickEvent = document.querySelector('DIV#toggle_header');
clickEvent.onclick = function () {

    if (colorChange.classList.contains('red')) {
        colorChange.classList.remove('red');
        colorChange.classList.add('green');
    }
    else {
        colorChange.classList.remove('green');
        colorChange.classList.add('red');
    }
};

