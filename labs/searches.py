"""
searches.py

A Python module containing various search algorithms.

Author: James Quinlan
Date: 	11/24/2023

List of Search Algorithms:
1. Binary Search
2. Linear Search

Usage:
- Import the module using 'import searches'
- Use the individual search functions, e.g., 'searches(arr, target)'
- Alternatively, copy and paste in Colab cell

Note: Binary Search requires the input list to be sorted.

"""

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def binary_search(data, target):
  """
  ----------------------------------------------------------------------------
  Perform a binary search on a sorted list to find the index of the target element.

  Parameters:
  - data (list): The sorted input list to be searched.
  - target: The element to search for in the list.

  Returns:
  - int: The index of the target element if found, or -1 if not.

  Binary Search exploits the fact that the list is sorted. It repeatedly divides the
  search interval in half until the target element is found or the interval becomes empty.

  Note: To work correctly, the input list must be sorted for binary search.

  Example:
  >>> data = [1, 2, 3, 4, 7, 9]
  >>> binary_search(data, 7)
  4
  """
  low, high = 0, len(data) - 1
  while low <= high:
    mid = (low + high) // 2
    if data[mid] == target:
      return mid
    elif data[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  return -1  


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def linear_search(data, target):
  """
  ----------------------------------------------------------------------------
  Perform a linear search on a list to find the index of the target element.

  Parameters:
  - data (list): The input list to be searched.
  - target: The element to search for in the list.

  Returns:
  - int: The index of the target element if found, or -1 if not found.
  Linear Search iterates through each element in the list sequentially and compares
  it with the target element until a match is found or the end of the list is reached.

  Example:
  >>> data = [4, 2, 7, 1, 9, 3]
  >>> linear_search(data, 7)
  2
  """
  for i, value in enumerate(arr):
    if value == target:
      return i
  return -1
