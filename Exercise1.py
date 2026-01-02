# Uses an internal (nested) function to perform a recursive binary search.
# The inner function handles the search logic while accessing the outer
# function’s variables, keeping the code clean and well-organized.

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
    st=0
    fin = len(array) - 1
    return binary_search_internal(st,fin)



my_list = [i*i for i in range(10)]
print(my_list)
print(binary_search(my_list, 3))
