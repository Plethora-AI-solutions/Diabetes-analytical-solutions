

function alertShow() {

    const Alert1 = document.getElementById("Alert1");
    
    Alert1.classList.add("openAlert");

    }

window.addEventListener("load", alertShow())


Clsb = document.getElementById("popB")

function alertClose() {

    const Alert1 = document.getElementById("Alert1");
    
    Alert1.classList.remove("openAlert");

    }

Clsb.addEventListener('click', alertClose)


