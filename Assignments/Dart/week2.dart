// The program should demonstrate an understanding of data types in Dart.
// Implement the data types you have learned in the previous lesson.

// Requirements
// The program should demonstrate an understanding of data types in Dart,
// including int, double, String, List, and Map.
// The program should include at least one example of each data type.
// The program should include comments to explain each data type and its use.


void main() {

   // Strings
  String name = 'John Doe';
  String greeting = 'Hello, Dart!';

  // integers 
  int age = 25;
  int numberOfApples = 10;
  
  // doubles
  double temperature = 36.5;
  double piValue = 3.14;
  
  // Lists: 
  List<int> numbers = [1, 2, 3, 4, 5];
  List<String> fruits = ['apple', 'banana', 'orange'];
  
  // Maps
  Map<String, int> studentGrades = {'Math': 90, 'Science': 85, 'English': 88};
  Map<String, dynamic> personInfo = {
    'name': 'Alice',
    'age': 30,
    'isEmployed': true
  };
  
  // Code Output
  print('Age: $age');
  print('Number of apples: $numberOfApples');
  
  print('Temperature: $temperature');
  print('Value of pi: $piValue');
  
  print('Name: $name');
  print('Greeting: $greeting');
  
  print('Numbers: $numbers');
  print('Fruits: $fruits');
  
  print('Student Grades: $studentGrades');
  print('Person Info: $personInfo');
}
