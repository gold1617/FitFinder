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
      console.log(data.age);
    document.getElementById("age").value = Number(data.age);
    document.getElementById("height").value=data.height;
    document.getElementById("name").value=data.name;
    document.getElementById("bio").value=data.bio;
  });
}

function accountInfo(){
    document.getElementById('id02').style.display='block';
    getData();
}
