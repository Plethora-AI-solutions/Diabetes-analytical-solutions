
/*const dclick = document.getElementById('dclick');


function alertShow() {

    const Alert1 = document.getElementById("Alert1");
    
    Alert1.classList.add("openAlert");

    }

window.addEventListener("load", alertShow)*/

const now =  new Date();
const hours = now.getHours();
let userGreeting = document.getElementById('greet');



function greetUser() {

    if (hours < 12 ) {

        return userGreeting.innerHTML = 'Good Morning!'

    }
    else if( hours < 18) {

        return userGreeting.innerHTML = 'Good Afternoon!'

    }
    else {
        return userGreeting.innerHTML = 'Good Evening!'
    }

}

window.addEventListener('load', greetUser);


  
function backCol(){

    const results = document.getElementById("table").rows[9].cells[1]
    const backgcol = document.getElementById("table").rows[9].cells[1]

    if (results.innerText === 'Negative') {

        backgcol.style.backgroundColor='green'
    }

    else {
        backgcol.style.backgroundColor= 'red'
    }
}
