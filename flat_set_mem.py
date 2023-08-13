import random
import string
from memory_profiler import profile

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

num = 100000
@profile
def create_set_dictionary(num):
  num_entries = num
  max_key_length = 10
  max_value_length = 20

  set_of_tuples = set()

  while len(set_of_tuples) < num_entries:
      key_length = random.randint(1, max_key_length)
      value_length = random.randint(1, max_value_length)
      key = generate_random_string(key_length)
      value = generate_random_string(value_length)
      set_of_tuples.add((key, value))

  # Printing the first few key-value pairs
  count = 0
  for key, value in set_of_tuples:
      print(f"{key}: {value}")
      count += 1
      if count >= 5:  # Displaying the first 5 entries
          break
      
if __name__ == '__main__':
  create_set_dictionary(num)
  create_set_dictionary(num+1)
  create_set_dictionary(num+2)
  create_set_dictionary(num+3)
  create_set_dictionary(num+4)
