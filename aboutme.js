//first button on first row
// Get the modal
var modal1 = document.getElementById('myModal1');

// Get the button that opens the modal
var btn_1_1 = document.getElementById("myBtn_1_1");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal
btn_1_1.onclick = function() {
     modal1.style.display = "block";
 }

//When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal1.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal1) {
        modal1.style.display = "none";
    }
}
//first button on second row
var modal2 = document.getElementById('myModal2');

var btn_2_1 = document.getElementById("myBtn_2_1");

var span = document.getElementsByClassName("close")[1];

btn_2_1.onclick = function() {
    modal2.style.display = "block";
}

span.onclick = function() {
    modal2.style.display = "none";
}
//second button on second row
var modal3 = document.getElementById('myModal3');

var btn_2_2 = document.getElementById("myBtn_2_2");

var span = document.getElementsByClassName("close")[2];

btn_2_2.onclick = function() {
    modal3.style.display = "block";
}

span.onclick = function() {
    modal3.style.display = "none";
}

//first left button on third row
var modal4 = document.getElementById('myModal4');

var btn_3_1 = document.getElementById("myBtn_3_1");

var span = document.getElementsByClassName("close")[3];

btn_3_1.onclick = function() {
    modal4.style.display = "block";
}

span.onclick = function() {
    modal4.style.display = "none";
}

//second button on third row
var modal5 = document.getElementById('myModal5');

var btn_3_2 = document.getElementById("myBtn_3_2");

var span = document.getElementsByClassName("close")[4];

btn_3_2.onclick = function() {
    modal5.style.display = "block";
}

span.onclick = function() {
    modal5.style.display = "none";
}

//third button on third row
var modal6 = document.getElementById('myModal6');

var btn_3_3 = document.getElementById("myBtn_3_3");

var span = document.getElementsByClassName("close")[5];

btn_3_3.onclick = function() {
    modal6.style.display = "block";
}

span.onclick = function() {
    modal6.style.display = "none";
}
