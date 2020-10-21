//similar to dictionaries, unordered key-value pairs
var carInfo = {make: "toyota", year: 1990, model:"camry"}
carInfo["make"]

//arryas and objects in objects
var myNewO = {a:"hello",b:[1,2,3],c:{inside:['a','b']}}
myNewO['a']
myNewO['b'][2]
myNewO['c']['inside'][1]

//changing key values
carInfo['year'] = 2006;

//loops with objects, key value pairs are unordered
for (i in carInfo){
    console.log(i)
    console.log(carInfo[i])
}