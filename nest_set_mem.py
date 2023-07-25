import sys
from memory_profiler import profile

@profile
def create_nested_set(keys_per_level, depth, final_level_keys):
    if depth == 0:
        return None
    else:
        nested_set = set()
        if depth == 1:
            # For the last (most nested) level, create a set with 'final_level_keys' elements.
            for i in range(final_level_keys):
                nested_set.add(f"key_{i}")
        else:
            # For other levels, create a set with one element and call the function recursively.
            nested_set.add(create_nested_set(keys_per_level, depth - 1, final_level_keys))
        return nested_set

def print_nested_set(nested_set, indentation=""):
    for i, item in enumerate(nested_set):
        if isinstance(item, set):
            print(f"{indentation}Level {i}:")
            print_nested_set(item, indentation + "  ")
            print(f"{indentation}")
        else:
            print(f"{indentation}Level {i}: {item}")

# Example usage:
num_nested_levels = 4  # Change this value to control the number of nested levels (excluding the most nested level).
keys_per_level = 1  # Each level, except the last, will have one element.
final_level_keys = 10000  # The most nested level will have 10,000 elements.

if __name__ == '__main__':
  create_nested_set(keys_per_level, num_nested_levels, final_level_keys)

