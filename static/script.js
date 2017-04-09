/*Login Functions and Var*/
// Get the modal
var modal = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

function sendData (){

}

function getData(){
  $.get("/myprofile",function(data, status){
    document.getElementByName("age").value=(data.age);
    document.getElementByName("height").value=(data.height);
    document.getElementByName("name").value=(data.name);
    document.getElementByName("bio").value=(data.bio);
  });
}

function accountInfo(){
  getData();
  document.getElementById('id02').style.display='block';
}
