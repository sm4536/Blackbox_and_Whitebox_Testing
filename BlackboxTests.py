# -----------------------------------------------------------------------------------------------------------------------------
# I divided the inputs into valid and invalid equivalence input spaces.
# For invalid case, I have used char array.
# For valid case, I further divided inputs based on lenght of array into even and odd.
# Finally i tested bourndary conditions by choosing target element from first, mid and last position of array
# and exceptional cases like saving same element twice in the array
#
# -----------------------------------------------------------------------------------------------------------------------------
import pytest
import binarySearch

def test_for_invalid_input():
    arr = ['a','b','c','d','e']
    x = "f"
    user_output = binarySearch.binary_search(arr,x)
    assert user_output == -1,"test Passed"

def test_for_valid_input():
    arr = ['a','b','c','d','e']
    x = "e"
    user_output = binarySearch.binary_search(arr,x)
    assert user_output == 4,"test Passed"

def test_for_even_length_array_with_element_in_first_half():
    arr = [1,2,3,4,5,6,7,8,9,10]
    x = 1
    user_output = binarySearch.binary_search(arr,x)
    assert user_output == 0,"test Passed"

def test_for_odd_length_array_with_element_in_middle():
    arr = [1,2,3,4,5,6,7]
    x = 3
    user_output = binarySearch.binary_search(arr,x)
    assert user_output == 2,"test Passed"

def test_for_odd_length_array_with_last_element():
    arr = [1,2,3,4,5,6,7,10,12,15,17,18,20]
    x = 20
    user_output = binarySearch.binary_search(arr,x)
    assert user_output == 12,"test Passed"

def test_for_array_with_equal_elements():
    arr = [1,2,3,4,5,5,6,7,8]
    x = 5
    user_output = binarySearch.binary_search(arr,x)
    assert user_output == 4,"test Passed"
