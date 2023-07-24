import sys
from memory_profiler import profile

OBJ_SIZE = 1000
FILLING = 10


@profile
def amplify_object(initial_obj, amplif_num):
    print(f"Expanding the original object by a factor of: {amplif_num}")
    for idx in range(1, amplif_num + 1):
        for inner_idx in range(OBJ_SIZE):
            # add leading zeros to ensure the same string size
            number_str = str(idx * 100 + inner_idx).zfill(FILLING)
            key_name = f"This_Key_{number_str}"
            value_name = f"Value_{number_str}"
            initial_obj[key_name] = value_name
    # return original object, which has now mutated
    return initial_obj


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("You need to provide the amplification factor. E.g.: python flat_dict_mem.py 100")
        sys.exit(1)
    amplif = int(sys.argv[1])

    my_dict = {}
    for idx in range(OBJ_SIZE):
        # add leading zeros to ensure the same string size
        number_str = str(idx).zfill(FILLING)
        key_name = f"This_Key_{number_str}"
        value_name = f"Value_{number_str}"
        my_dict[key_name] = value_name

    result = amplify_object(my_dict, amplif)
