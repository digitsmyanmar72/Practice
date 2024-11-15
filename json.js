//Json string to Json object
const person1 = '{"name":"nay","age":43}';
const person2 =JSON.parse(person1)

console.log(person2.name)
//JS object to Json string
const p1 = {name:"nay",age:41};
const p2 = JSON.stringify(p1)
console.log(p2)