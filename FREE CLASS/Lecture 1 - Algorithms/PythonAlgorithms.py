
def select_sort(numbers: list) -> list:
    """

    This function takes in an unsorted list and uses the selection sort algorithm to sort it
    :return: A sorted list
    """
    for i in range(len(numbers) -1):
        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j

        temp = numbers[i]
        numbers[i] = numbers[min_index]
        numbers[min_index] = temp

    return numbers


def bsearch(array: list, num_search: int, first: int, last: int) -> bool:
    """

        This function takes in a sorted list,number to search,first and last index of the list then uses the binary search algorithm to find
        the number
        :return: True or False
        """
    if abs(first - last) < 2:
        return array[first] == num_search or array[last] == num_search
    mid = int((first + last) / 2)
    if array[mid] == num_search:
        return True
    if num_search < array[mid]:
        return bsearch(array, num_search, first, mid)
    return bsearch(array, num_search, mid, last)


def binarysearch(array, num_search):
    """
        This function takes in a sorted list and number to search then uses the binary search algorithm to find
        the number
        :return: True or False
    """

    return bsearch(array, num_search, 0, len(array) - 1)



if __name__ == "__main__":
    # using binary search algorithm to search for a number in a list
    print(".........Staring binary search...........")
    array = [1, 3, 10, 32, 57]
    num_search = 10
    print(f"Found: {binarysearch(array, num_search)}")

    # sorting an array using the selection sort algorithm
    print("\n.......Selection sort.........")
    unSortedArray = [3, 2, 65, 1, 0]
    print("Sorted Array: {}".format(select_sort(unSortedArray)))

  
