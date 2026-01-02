
def binary_search(array, x):

    def binary_search_internal(start,finish):
        middle = (start + finish) // 2
        if start <= finish:
            if x == array[middle]:
                return middle
            elif x < array[middle]:
                return binary_search_internal(start, middle - 1)
            else:  # x > array[middle]
                return binary_search_internal(middle + 1, finish)
        else:
            return -1
    start=0
    finish=len(array)
    return binary_search_internal(start,finish)



my_list = [i*i for i in range(10)]
print(my_list)
print(binary_search(my_list, 3))
