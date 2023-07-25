import random
import string
import sys
from memory_profiler import profile


def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

@profile
def create_flat_dictionary():
  num_entries = 10000
  max_key_length = 10
  max_value_length = 20

  list_of_tuples = []

  for _ in range(num_entries):
      key_length = random.randint(1, max_key_length)
      value_length = random.randint(1, max_value_length)
      key = generate_random_string(key_length)
      value = generate_random_string(value_length)
      list_of_tuples.append((key, value))

  # Printing the first few key-value pairs
  for idx, (key, value) in enumerate(list_of_tuples):
      print(f"{key}: {value}")
      if idx >= 4:  # Displaying the first 5 entries
          break


if __name__ == '__main__':
  create_flat_dictionary()