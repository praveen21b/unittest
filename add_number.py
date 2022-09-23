import math


def add_number_max(number,target = 5):
    num_str = str(number)
    mode, targ_str = (1,num_str) if number >= 0 else (-1,num_str[1:])
    max_val = -math.inf # fixed max values as negative infinity

    for i in range(0, len(targ_str)+1):
        generated_string = targ_str[:i] + str(target) + targ_str[i:]
        max_val = max(max_val,(mode*int(generated_string)))

    return max_val

if __name__ == '__main__':
    print(add_number_max(128))#5128
    print(add_number_max(-128))#-1258