// Restart Game
var restartGame = document.querySelector("#b");

// Grab All squares
var squares = document.querySelectorAll("td");

// Clear all squares
function clearBoard() {
    for (var i=0; i < squares.length; i++) {
        squares[i].textContent = "";
    }
}

restartGame.addEventListener('click', clearBoard)

// Check square marker
function changeMarker() {
    if(this.textContent === "") {
        this.textContent = "X"
    } else if (this.textContent === "X") {
        this.textContent = "O";
    } else {
        this.textContent = "";
    }
}

// For loop to add even listeners to all the squares
for (var i=0; i < squares.length; i++) {
    squares[i].addEventListener('click',changeMarker)
}