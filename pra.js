function Person(first, last, age, eye) {
    this.firstName = first;
    this.lastName = last;
    this.age = age;
    this.eyeColor = eye;
  }
  
  // Create a Person object
  const myFather = new Person("John", "Doe", 50, "blue");
  const mother = new Person ("a","b",4,"d")

 const x = myFather;
 const y = mother;
 console.log(x);
 console.log(y)
 