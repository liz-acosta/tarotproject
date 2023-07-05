function loadCards() {
    // Show loading animation while final reading is rendered 
    
    var loadingDiv = document.getElementById("loading");
    var cardTable = document.getElementById("card-table");

    cardTable.style.display = "none";
    
    loadingDiv.style.display = "block";
    loadingDiv.style.animation = "fadein 2s";
}