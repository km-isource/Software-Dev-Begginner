void main(List<String> arguments) {
  if (arguments.isNotEmpty) {
    int? number = int.tryParse(arguments[0]);

    if (number != null) {
      if (number > 10) {
        print('Your number is greater than 10');
      } else if (number < 10) {
        print('Your number is less than 10');
      } else {
        print('Your number is equal to 10');
      }
    } else {
      print('Invalid input. Please enter a valid number.');
    }
  } else {
    print('No number provided. Please provide a number as a command-line argument.');
  }
}
