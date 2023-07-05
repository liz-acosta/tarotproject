// Set clicks and cards counters
var clicks = 3;
var flippedCards = 3;

// Get context from template
// TODO: Use session for this
var data = JSON.parse(document.getElementById('finalCards').textContent);
var tarotReading = JSON.parse(document.getElementById('tarotReading').textContent);

function flipCard(cardID) {
    // Keep track of the number of clicks and cards flipped
    // Flip cards as they are clicked/replace with image of card and reading
    // When three cards have been flipped,
    // make the tarot-reading div visible

    clicks = clicks - 1;
    flippedCards = flippedCards - 1;
    var flippedCard = data[flippedCards]
    
    if (flippedCard !== undefined) {
        var cardImage = "/static/tarotapp/images/tarot_deck/" + flippedCard['card_image'];
        var card = document.getElementById(cardID);
        card.src = cardImage;
        card.style.height = '250px';
        card.style.width = '142px';
        
        var p = document.createElement("p");
        var node = document.createTextNode(flippedCard['card_meaning']);
        p.append(node);
        card.after(p);
    }

    if (clicks == 0) { 
        // Once 3 cards have been selected/flipped over
        // make tarot-reading div visible
        // update card:hover opacity to 1

        // Get tarot-reading div
        var tarotReadingDiv = document.getElementById('tarot-reading');
        tarotReadingDiv.style.display = 'block';

        // Update card cover style so they no longer fade out
        var css = '.card:hover{ opacity: 1; }';
        var style = document.createElement('style');
        
        if (style.styleSheet) {
            style.styleSheet.cssText = css;
        } else {
            style.appendChild(document.createTextNode(css));
        }
        
        document.getElementsByClassName('card')[0].appendChild(style);        
    }
  }