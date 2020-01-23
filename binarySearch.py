

def binary_search(array, needed_element):
    first =0
    last = len(array)
    while first < last:
        x = first + (last - first) // 2
        val = array[x]
        if needed_element == val:
            return x
        elif needed_element > val:
            if first == x:
                break
            first = x
        elif needed_element < val:
            last = x
    return -1

binary_search([1,2,3,4,5],2)
binary_search([15,16,17,18,19],18)
binary_search([5,6,7,8,9],9)
binary_search([1,2,3,4,5],6)
