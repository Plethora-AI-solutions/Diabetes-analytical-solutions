

function backCol(){

    const results = document.getElementById("table").rows[9].cells[1]
    const backgcol = document.getElementById("table").rows[9].cells[1]

    if (results.innerText === 'Negative') {

        backgcol.style.backgroundColor='lightgreen'
    }

    else {
        backgcol.style.backgroundColor= 'red'
    }
}


/*window.addEventListener("load", backCol());


function alertme() {
    alert('We wish you all the best in your results!')
}

window.addEventListener('load', alertme())*/
