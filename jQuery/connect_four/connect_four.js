var player1 = prompt("P1 Enter Name, you will be Blue");
var player1Color = 'rgb(86, 151, 255)';

var player2 = prompt("P2 Enter Name, you will be Red");
var player2Color = 'rgb(237, 45, 73)';

var game_on = true;

// Select table tr using jquery syntax
var table = $('table tr');

// For debugging purposes
function reportWin(rowNum, colNum) {
    console.log("You won starting at this row, col");
    console.log(rowNum);
    console.log(colNum);
}

// Change the button color for a certain row and col index
function changeColor(rowIndex, colIndex, color) {
    return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color',color);
}

// Find the color
function reportColor(rowIndex, colIndex) {
    return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color');
}

// Take in column index, returns the bottom row that is still gray
function checkBotton(colIndex) {
    var colorReport = reportColor(5, colIndex);
    for (var row = 5; row > -1; row--) {
        colorReport = reportColor(row, colIndex);
        if (colorReport === 'rgb(128, 128, 128)') {
            return row
        }
    }
}

// Check to see if 4 inputs are the same color
function colorMatchCheck(one, two, three, four) {
    return (one === two && one === three && one === four && one !== 'rgb(128, 128, 128)' && one !== undefined);
}

// Check for Horizontal Wins
function horizontalWinCheck() {
    for (var row = 0; row < 6; row++) {
      for (var col = 0; col < 4; col++) {
        if (colorMatchCheck(reportColor(row,col), reportColor(row,col+1) ,reportColor(row,col+2), reportColor(row,col+3))) {
          console.log('horiz');
          reportWin(row,col);
          return true;
        }else {
          continue;
        }
      }
    }
}
  

// Check for Vertical Wins
function verticalWinCheck() {
    for (var col = 0; col < 7; col++) {
      for (var row = 0; row < 3; row++) {
        if (colorMatchCheck(reportColor(row,col), reportColor(row+1,col) ,reportColor(row+2,col), reportColor(row+3,col))) {
          console.log('vertical');
          reportWin(row,col);
          return true;
        }else {
          continue;
        }
      }
    }
}

// Check for Diagonal Wins
function diagonalWinCheck() {
    for (var col = 0; col < 5; col++) {
      for (var row = 0; row < 7; row++) {
        if (colorMatchCheck(reportColor(row,col), reportColor(row+1,col+1) ,reportColor(row+2,col+2), reportColor(row+3,col+3))) {
          console.log('diag');
          reportWin(row,col);
          return true;
        }else if (colorMatchCheck(reportColor(row,col), reportColor(row-1,col+1) ,reportColor(row-2,col+2), reportColor(row-3,col+3))) {
          console.log('diag');
          reportWin(row,col);
          return true;
        }else {
          continue;
        }
      }
    }
}

// Game End
function gameEnd(winningPlayer) {
    for (var col = 0; col < 7; col++) {
      for (var row = 0; row < 7; row++) {
        $('h3').fadeOut('fast');
        $('h2').fadeOut('fast');
        $('h1').text(winningPlayer+" has won! Refresh your browser to play again!").css("fontSize", "50px")
      }
    }
}

// Start with player 1
var currentPlayer = 1;
var currentName = player1;
var currentColor = player1Color;

// Change heading to indicate player 1
$('h3').text(player1 + " it is your turn!")

// What happens when a button is clicked
$('.board button').on('click', function(){

    var col = $(this).closest('td').index();
    // check the closet button for its color
    var bottomAvail = checkBotton(col);

    //change color
    changeColor(bottomAvail,col, currentColor);

    //win check
    if (horizontalWinCheck() || verticalWinCheck() || diagonalWinCheck()) {
        $('h1').text(currentName + " You have won!")
        $('h3').fadeOut('fast');
        $('h2').fadeOut('fast');
    }
      
      // cycle through players
    currentPlayer = currentPlayer * -1;

    if (currentPlayer === 1) {
        currentName = player1;
        $('h3').text(currentName + " it is your turn");
        currentColor = player1Color;
    } else {
        currentName = player2;
        $('h3').text(currentName + " it is your turn");
        currentColor = player2Color;
    }
  })