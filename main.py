"""Min Max Difference
In this problem you will be given an array/list of integers. You need to find the largest value and the smallest value in the array. Finally you need to return the difference (largest value - smallest value) of the two values.
Example:
the_array = [15, 22, 84, 14, 88, 23]
the_highest_value = 88
the_smallest_number = 14
the_difference = 74"""


def the_highest_value(my_array):
    highest_value = my_array[0]
    for value in my_array:
        if value >= highest_value: highest_value = value

    return highest_value

def the_smallest_value(my_array):
    highest_value = my_array[0]
    for value in my_array:
        if value <= highest_value: highest_value = value

    return highest_value

def the_difference(my_array):

    difference = the_highest_value(my_array) - the_smallest_value(my_array)

    return difference

def main():
    the_array = [15, 22, 84, 14, 88, 23]
    print(the_highest_value(the_array))
    print(the_smallest_value(the_array))
    print(the_difference(the_array))
    return None

if __name__ == "__main__":
    main()