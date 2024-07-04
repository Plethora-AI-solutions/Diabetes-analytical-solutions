
/*$('#form').on('submit', function(e) {

    
   
  $.ajax({

    url: "{% url 'register' %}", 
    data : form.serialize(), 
    type: "POST", 
    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
    success: function(response
    ) {


      consol.log(response)



    }, 

    error: function(response) {

      console.log(response.data)
    }
   


})*/


/*regSubmit.addEventListener('error', (e) => {

  e.preventDefault();

})*/


  
/*$('#fname').on("error", function(e) {

  e.preventDefault();
 

})



$('#fname').on('change', function() {

  console.log( $(this).val() )
})



function validateForm (e) {

  let Fname = document.getElementById('fname')
  let Sname = document.getElementById('sname')

  if (Fname.value < 2) {

  e.preventDefault();
  }
}

reForm = document.getElementById('formm')

reForm.addEventListener('submit', validateForm())*/


const Formm = document.getElementById('formm');
var fnameError = document.getElementById('fname-error');
var snameError = document.getElementById('sname-error');
var passError = document.getElementById('pass-error');
var passErrorCon = document.getElementById('pass-error');



function validate(e) {

  var Fname = document.getElementById('fname').value;
  var Sname = document.getElementById('sname').value;
  var regPass = document.getElementById('pass1').value;
  var regPass2 = document.getElementById('pass2').value;
  var errorMessages = document.getElementById('error-messages');



  if(Fname.length < 2) {


    document.getElementById('fname').style.border = "medium solid #f70202";

    document.getElementById('fname').style.color="red";
    errorMessages.style.backgroundColor='red';
    fnameError.innerHTML = '*First name MUST be more than one character!';
    e.preventDefault();
  }
    else {
      

      function RemoveData() {

      document.getElementById('fname').style.border = "";
      document.getElementById('fname').style.color="";
      fnameError.innerHTML = ''


      }


      document.getElementById('fname').addEventListener('keyup', RemoveData);

      
      

    }

  if(Sname.length < 2 ) {

    document.getElementById('sname').style.border = "medium solid #f70202";
    document.getElementById('sname').style.color="red";
    snameError.innerHTML = '*Last name MUST be more than one character!';
    e.preventDefault();
  }
    else {

      document.getElementById('sname').style.border = '';
      document.getElementById('sname').style.color ='';
      snameError.innerHTML = '';
    }
   

  if(regPass.length < 8) {

    document.getElementById('pass1').style.border = "medium solid #f70202";
    passError.innerHTML = '*Password MUST be greater than 8!'
    errorMessages.style.backgroundColor='red';
    e.preventDefault();

  }

  if(regPass2 != regPass) {


    document.getElementById('pass2').style.border = "medium solid #f70202";
    document.getElementById('pass1').style.border = "medium solid #f70202";
    passErrorCon.innerHTML = '*Passwords does not MATCH!'
    errorMessages.style.backgroundColor='red';
    e.preventDefault();
  }


}


Formm.addEventListener('submit', validate)

