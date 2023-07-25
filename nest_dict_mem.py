import sys
from memory_profiler import profile

num_nested_levels = 4  # Change this value to control the number of nested key-value pairs (excluding the most nested level).
keys_per_level = 1  # Each level, except the last, will have one key-value pair.
final_level_keys = 10000  # The most nested level will have 10,000 key-value pairs.

@profile
def create_nested_dictionary(keys_per_level, depth, final_level_keys):
    if depth == 0:
        return None
    else:
        nested_dict = {}
        if depth == 1:
            # For the last (most nested) level, create a dictionary with 'final_level_keys' keys and their corresponding values as None.
            for i in range(final_level_keys):
                nested_dict[f"key_{i}"] = None
        else:
            # For other levels, create a single key-value pair and call the function recursively.
            nested_dict["key"] = create_nested_dictionary(keys_per_level, depth - 1, final_level_keys)
        return nested_dict

def print_nested_dictionary(dictionary, indentation=""):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            print(f"{indentation}{key}:")
            print_nested_dictionary(value, indentation + "  ")
        else:
            print(f"{indentation}{key}: {value}")

if __name__ == '__main__':
  create_nested_dictionary(keys_per_level, num_nested_levels, final_level_keys)


my_dict = create_nested_dictionary(keys_per_level, num_nested_levels, final_level_keys)
#neprint_nested_dictionary(my_dict)