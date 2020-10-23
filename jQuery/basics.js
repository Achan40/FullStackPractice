// Selecting w jQuery
var x = $('h1')

// CSS one property
x.css('color','red')

// CSS multiple properties
// Create JS object for CSS prperties
var newCSS = {
    'color' : 'white',
    'background' : 'blue',
    'border' : '20px solid red'
}

x.css(newCSS)

// Selecting multiple objects with jquery
var listItems = $('li')

// all items
listItems.css('color','blue')

// one items use eq by indexing
listItems.eq(0).css('color','orange')

// Grabbing text
$('h1').text("BRAND NEW TEXT")
//changing html
$('h1').html("<em>new</em>")

// Grabbing input and affecting attribute
$('input').eq(1).attr('type','checkbox')

// affecting value
$('input').eq(0).val('new value!')

// adding a class 
$('h1').addClass('turnRed')
// remove class
$('h1').removeClass('turnRed')
// toggle class
$('h1').toggleClass('turnBlue')


// EVENTS SEE:https://api.jquery.com/category/events/
$('h1').click(function(){
    console.log('There was a click!');
})

$('li').click(function(){
    console.log('any li was clicked!');
})

// Call methods or properties off any variables
$('h1').click(function () {
    $(this).text("I was changed!");
})

// Key Press
$('input').eq(0).keypress(function() {
    // when enter key is pressed in input box, toggle the class to blue
    if (event.which === 13) {
        $('h3').toggleClass('turnBlue')
    }
    // log in console infomation when event occurs
    console.log(event);
})

// the on() method
$('li').on('dblclick',function(){
    $(this).toggleClass('turnBlue')
})

// Events and animations
$('input').eq(1).on('click',function(){
    $('.container').fadeOut('3000')
})