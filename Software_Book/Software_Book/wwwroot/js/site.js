// Please see documentation at https://docs.microsoft.com/aspnet/core/client-side/bundling-and-minification
// for details on configuring this project to bundle and minify static web assets.

// Write your JavaScript code.

function displayCalander() {
    area = document.getElementById("governate").value;
    console.log(area)
    switch (area) {
        case "hawally":
            document.getElementById("calendar-a").style.display = "block";
            document.getElementById("calendar-b").style.display = "none";
            document.getElementById("calendar-c").style.display = "none";
            break;
        case "city":
            document.getElementById("calendar-b").style.display = "block";
            document.getElementById("calendar-a").style.display = "none";
            document.getElementById("calendar-c").style.display = "none";
            break;
        case "ahmadi":
            document.getElementById("calendar-c").style.display = "block";
            document.getElementById("calendar-a").style.display = "none";
            document.getElementById("calendar-b").style.display = "none";
            break;
        default:
            console.log("Invalid Area selected");
    }
}


function userselected_message() {
    var customerName = document.getElementById("customer_selecter_button").value;
    alert("Selected customer name is: " + customerName);
}



