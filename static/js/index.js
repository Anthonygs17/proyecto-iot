$(document).ready(function () {
    console.log("index.js loaded");

    $.ajax({
        url: `/feeding-data`,
        method: "GET",
        dataType: "json",
        contentType: "application/json",
        success: function (data) {
            console.log(data);
            document.getElementById("main-div").innerHTML+= "<h2>Comida: "+data.comida+" g</h2>";
            document.getElementById("main-div").innerHTML+= "<h2>Agua: "+data.agua+" ml</h2>";
        },
    });

});