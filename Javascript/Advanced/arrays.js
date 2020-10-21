//arryas are mutable
//strings are immutable

var countries = ["US", "Canada", "Brazil"]

//arrays take mixed data types
var mixed = [true,20,"string"]
mixed.length

var nestedArray = [[1,2,3],[4,5,6]]

//loops with arrays
var arr = ["A","B","C"]
for (var i = 0; i<arr.length; i++){
    console.log(arr[i]);
}

// for of lets you loop through array
for (letter of arr){
    console.log(letter);
}

// for Each is similar as well
// for instance, this will send out an alert for each element in arr
arr.forEach(alert);

// for Each using custom function
function addAwesome(name) {
    console.log(name + " is awesome!");
}

arr.forEach(addAwesome);