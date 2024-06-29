
/*function hello(){
    const a = document.getElementById("table").rows[1].cells[0]
    const b = document.getElementById('table').rows[1].cells[1]

    if(b.innerText === '1'){
    
    a.style.backgroundColor='blue';

    }

    else {
        a.style.backgroundColor='green';
    }


    }




function alertme() {
    alert('I will manage my diabetes')
}*/

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
        return userGreeting.innerHTML = 'Good evening!'
    }

}

window.addEventListener('load', greetUser);


  

