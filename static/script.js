/*Login Functions and Var*/
// Get the modal
var modal = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}


function getData(){
  $.get("/myprofile",function(data, status){
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

function getBuddy()
{
   $.get("/buddy",function(data, status){
        var myNode = document.getElementById("biobox");
        while (myNode.firstChild) {
                myNode.removeChild(myNode.firstChild);
        }
        var text = document.createTextNode("Name: " + data.name);        
        myNode.appendChild(text);
        text = document.createElement("br");
        myNode.appendChild(text);
        text = document.createTextNode("Age: " + data.age);
        myNode.appendChild(text);
        text = document.createElement("br");
        myNode.appendChild(text);
        text = document.createTextNode("Height: " + data.height);
        myNode.appendChild(text);
        text = document.createElement("br");
        myNode.appendChild(text);
        text = document.createTextNode("Bio: " + data.bio);
        myNode.appendChild(text);
        
        document.getElementById("profpic").setAttribute("src","static/images/"+data.name+".jpg");

   });  
}
