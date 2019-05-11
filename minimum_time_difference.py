
def minimum_time_difference(timeInstants):
  #
  # IMPORTANT:
  # 1. Write your solution in this function
  # 2. Do not make changes to the function signature
  # 3. Use the 'run' command in the IDE, to run the main method. You can also invoke the main method from the terminal.
  # 4. Use the 'run-tests' command in the IDE, to run unit tests.
  return None


def main():
  timeInstants = ['11:00','12:02','11:58']
  minimum_value = minimum_time_difference(timeInstants)
  message = 'Given time instant values {0}, minimum difference between any two time instants is {1}\n'.format(
      timeInstants, minimum_value)
  print(message)


if __name__ == '__main__':
  main()