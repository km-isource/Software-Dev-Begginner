// Task 1
// Write a function called addTwo that takes two numbers as arguments 
// and returns the sum of those two numbers.

int addTwo(int num1, int num2) {
  return num1 + num2;
}



// Task 2
// Write a function called subtractTwo that takes two numbers
// as arguments and returns the difference of those two numbers.

int subtractTwo(int num1, int num2) {
  return num1 - num2;
}


// Task 3
// Write a function called multiplyTwo that takes two numbers as
// arguments and returns the product of those two numbers.

int multiplyTwo(int num1, int num2) {
  return num1 * num2;
}


// Task 4
// Write a function called divideTwo that takes two numbers as
//arguments and returns the quotient of those two numbers.

double divideTwo(double num1, double num2) {
  if (num2 != 0) {
    return num1 / num2;
  } else {
    throw ArgumentError('Cannot divide by zero');
  }
}


// Task 5
// Write a function called stringLength that takes an argument of
// type String and returns the length of that string.

int stringLength(String str) {
  return str.length;
}



// Task 6
// Write a function called getFirstElement that takes
// a list as an argument and returns the first element of that list.

dynamic getFirstElement(List list) {
  if (list.isEmpty) {
    return null;
  } else {
    return list[0];
  }
}

void main() {
  print(addTwo(7, 21)); 
  print(subtractTwo(3, 4)); 
  print(multiplyTwo(9, 56));
  print(divideTwo(81, 9)); 
  print(stringLength("Hello World"));
  print(getFirstElement([1, 2, 3]));
}




