import string
import time
import gc
import psutil
import json
from memory_profiler import profile
from random import choices

def generate_random_string(length):
    return ''.join(choices(string.ascii_letters, k=length))

num = 20000
#@profile
def create_flat_dictionary(num):
  thisProcess = psutil.Process()
  startRss = thisProcess.memory_full_info().uss
  print(f"Creating flat dictionary with a total of {num} items")
  num_entries = num
  max_key_length = 10
  max_value_length = 20

  dictionary = {}

  for _ in range(num_entries):
      #key_length = random.randint(1, max_key_length)
      #value_length = random.randint(1, max_value_length)
      key = generate_random_string(max_key_length)
      value = generate_random_string(max_value_length)
      dictionary[key] = value

  # Printing the first few key-value pairs
  for idx, (key, value) in enumerate(dictionary.items()):
#      print(f"{key}: {value}")
      if idx >= 4:  # Displaying the first 5 entries
          break
  time.sleep(1)
  endRss = thisProcess.memory_full_info().uss
  totalUss = endRss - startRss
  totalUssMB = totalUss / (1024**2)
  print(f"Process with num: {num} had total USS: {totalUss} bytes ({totalUssMB} MB)")
  return (num, totalUssMB)


if __name__ == '__main__':
    results = []
    for i in range(0, 11):
        thisRes = []
        avgMem = 0
        thisRes.append(create_flat_dictionary(num * i))
        thisRes.append(create_flat_dictionary(num * i))
        thisRes.append(create_flat_dictionary(num * i))
        count = 3
        for item in thisRes:
            if item[1] < 0:
                print(f"BAD JOB: Num {item[0]} had a negative memory usage: {item[1]}")
                count -= 1
            avgMem += item[1]
        avgMem = avgMem / count
        results.append((num * i, avgMem))
    print(f"results: {results}")
    with open("mem_results.json", "r") as jobj:
        data = json.

    # append results 

    with open("mem_results.json", "w") as jobj:
        json.dump(results, jobj, indent=4)
