const now =  new Date();
const hours = now.getHours();
let userGreeting = document.getElementById('greet');



function greetUser() {

    if (hours < 12 ) {

        return userGreeting.innerHTML = 'Good morning!'

    }
    else if( hours < 18) {

        return userGreeting.innerHTML = 'Good afternoon!'

    }
    else {
        return userGreeting.innerHTML = 'Good evening!'
    }

}

window.addEventListener('load', greetUser);


  

