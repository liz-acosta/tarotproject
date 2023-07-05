var clicks = 3;
var flippedCards = 3;
const data = JSON.parse(document.getElementById('finalCards').textContent);
const tarotReading = JSON.parse(document.getElementById('tarotReading').textContent);

function flipCard(cardID) {

    clicks = clicks - 1;
    flippedCards = flippedCards - 1;

    var flippedCard = data[flippedCards]
    if (flippedCard !== undefined) {
        var cardImage = "/static/tarotapp/images/tarot_deck/" + flippedCard['card_image'];
        var card = document.getElementById(cardID);
        card.src = cardImage;
        card.style.height = '250px';
        card.style.width = '142px';
        
        const p = document.createElement("p");
        const node = document.createTextNode(flippedCard['card_meaning']);
        p.append(node);
        card.after(p);
    }
    if (clicks == 0) {
        
        // Once 3 cards have been selected/flipped over
        // get the div with id: tarot-reading and append
        // a p element populated with AI generated tarot reading,
        // a button element to do a new reading and
        // an option to text the reading to a user supplied phone number 

        // const tarotReading = document.getElementsByClassName('tarot-reading');

        // Get tarot-reading div
        const tarotReadingDiv = document.getElementById('tarot-reading');
        tarotReadingDiv.style.display = 'block';

        // Create elements
        // Create paragraph
        const tarotReadingP = document.createElement('p');
        tarotReadingP.textContent = tarotReading;
        
        // Create button
        const buttonText = "Change your fate!";
        const tarotReadingButton = document.createElement('button');
        tarotReadingButton.innerText = buttonText;
        tarotReadingButton.onclick = function () {
            document.location.pathname = "tarotapp/"
        };

        // Create text message form
        // const tarotReadingForm = 
        
        // Append elements
        // tarotReadingDiv.appendChild(tarotReadingP);
        // tarotReadingDiv.appendChild(tarotReadingButton);
    }
  }
  
  var myVar;
  
  function pageLoading() {

    myvar = setTimeout(loadPage, 3000);
  }

  function loadPage() {
    document.getElementById("loader").style.display = "none";
    document.getElementById("myDiv").style.display = "block";
  }