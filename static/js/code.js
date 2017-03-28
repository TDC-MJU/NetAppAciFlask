var fn_field = document.getElementById("first_name");

fn_field.onfocus = function () {
    if (fn_field.value == "Add _TN to the end of name"){
        fn_field.value = "";
        }

};

fn_field.onblur = function() {
    if (fn_field.value == "") {
        fn_field.value == "Add _TN to the end of name");


      }

};


function prepareEventHandlers() {
    document.getElementById("bdform").onsubmit = function() {
    if ( document.getElementById("email").value == "") {
        document.getElementById("emailerrormessage").innerHTML = "Please Provide a value";
        return false;
    }else {
         document.getElementByID("errormessage").innerHTML = "";
         return true;  
     }
    };
}





window.onload = function () {
    prepareEvenHandlers();
}
