
let headerToChange = document.querySelector('header');

let clickEvent = document.querySelector('DIV#update_header');

clickEvent.onclick = () => {
    headerToChange.innerHTML = "New Header!!!";
}