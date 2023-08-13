import random
import string
from memory_profiler import profile


def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

num = 100000
@profile
def create_flat_dictionary(num):
  num_entries = num
  max_key_length = 10
  max_value_length = 20

  dictionary = {}

  for _ in range(num_entries):
      key_length = random.randint(1, max_key_length)
      value_length = random.randint(1, max_value_length)
      key = generate_random_string(key_length)
      value = generate_random_string(value_length)
      dictionary[key] = value

  # Printing the first few key-value pairs
  for idx, (key, value) in enumerate(dictionary.items()):
      print(f"{key}: {value}")
      if idx >= 4:  # Displaying the first 5 entries
          break

if __name__ == '__main__':
  create_flat_dictionary(num)
  create_flat_dictionary(num+1)
  create_flat_dictionary(num+2)
  create_flat_dictionary(num+3)
  create_flat_dictionary(num+4)
  
