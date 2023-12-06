"""
sorts.py

A Python module containing various sorting algorithms.

Author: James Quinlan
Date:   11/24/2023

List of Sorting Algorithms:
1. Bubble Sort
2. Insertion Sort
3. Merge Sort
4. Quick Sort
5. Selection Sort

Usage:
- Import the module using 'import sorts'
- Use the individual sorting functions, e.g., 'sorts.bubble_sort(arr)'
- Alternatively, copy and paste entrie file in Colab cell or Jupyter NB

Note: Each sorting function sorts the input list in-place.
"""

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def bubble_sort(L):
  """
  ----------------------------------------------------------------------------
  Sorts a list in-place using the Bubble Sort algorithm.

  arameters:
  - arr (list): The input list to be sorted.

  Returns:
  - list: The sorted list.

  Bubble Sort repeatedly steps through the list, compares adjacent elements, and
  swaps them if they are in the wrong order. This process is repeated until the
  entire list is sorted.

  Example:
  >>> data = [4, 2, 7, 1, 9, 3]
  >>> bubble_sort(data)
  [1, 2, 3, 4, 7, 9]

  Time Complexity:
  - Best Case: O(n) when the list is already sorted.
  - Worst Case: O(n^2) when the list is in reverse order.
  - Average Case: O(n^2).

  Space Complexity:
  - O(1) as it sorts the list in-place.
  """

  n = len(A)
  for i in range(n-1):
    for j in range(1, n-i):
      if A[j] > A[j+1]:
        A[j], A[j+1] = A[j+1], A[j]  # Line 5



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def insertion_sort(A):
  """
  ----------------------------------------------------------------------------
  Sorts a list in-place using the Insertion Sort algorithm.

  Parameters:
  - A (list): The input list to be sorted.

  Returns:
  - list: The sorted list.

  Insertion Sort works by dividing the input list into a sorted and an unsorted
  region. It iterates over the unsorted region, comparing each element with the
  elements in the sorted region and inserting it at the correct position.

  Example:
  >>> data = [4, 2, 7, 1, 9, 3]
  >>> insertion_sort(data)
  [1, 2, 3, 4, 7, 9]

  Time Complexity:
  - Best Case: O(n) when the list is already sorted.
  - Worst Case: O(n^2) when the list is in reverse order.
  - Average Case: O(n^2).

  Space Complexity:
  - O(1) as it sorts the list in-place.
  """

  for i in range(1, len(A)):
    key = A[i]
    j = i - 1
    while j >= 0 and key < A[j]:
      A[j + 1] = A[j]
      j -= 1
      A[j + 1] = key
  return A



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def merge_sort(A):
  """
  ------------------------------------------------------------------------------
  Sorts a list in-place using the Merge Sort algorithm.

  Parameters:
  - arr (list): The input list to be sorted.

  Returns:
  - list: The sorted list.

  Merge Sort is a **divide-and-conquer** algorithm that recursively divides the
  input list into two halves, sorts each half, and then merges them back together.

  Example:
  >>> data = [4, 2, 7, 1, 9, 3]
  >>> merge_sort(data)
  [1, 2, 3, 4, 7, 9]

  Time Complexity:
  - Best Case: O(n log n) regardless of the input.
  - Worst Case: O(n log n) regardless of the input.
  - Average Case: O(n log n).

  Space Complexity:
  - O(n) for the additional space required during the merge call.
  """

  if len(A) > 1:
    mid = len(A) // 2
    left_half = A[:mid]
    right_half = A[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    i = j = k = 0

    while i < len(left_half) and j < len(right_half):
      if left_half[i] < right_half[j]:
        A[k] = left_half[i]
        i += 1
      else:
        A[k] = right_half[j]
        j += 1
        k += 1

    while i < len(left_half):
      A[k] = left_half[i]
      i += 1
      k += 1

    while j < len(right_half):
      A[k] = right_half[j]
      j += 1
      k += 1



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def quick_sort(A):
  """
  ----------------------------------------------------------------------------
  Sorts a list in-place using the Quick Sort algorithm.

  Parameters:
  - arr (list): The input list to be sorted.

  Returns:
  - list: The sorted list.

  Quick Sort is a divide-and-conquer algorithm that selects a pivot element and
  partitions the other elements into two sub-arrays according to whether they
  are less than or greater than the pivot. The process is applied recursively.

  Example:
  >>> data = [4, 2, 7, 1, 9, 3]
  >>> quick_sort(data)
  [1, 2, 3, 4, 7, 9]

  Time Complexity:
  - Best Case: O(n log n) when the pivot is chosen effectively.
  - Worst Case: O(n^2) when the pivot results in unbalanced partitions.
  - Average Case: O(n log n).

  Space Complexity:
  - O(log n) due to the recursive call stack.
  """

  if len(A) <= 1:
    return A
  pivot  = A[len(A) // 2]
  left   = [x for x in A if x < pivot]
  middle = [x for x in A if x == pivot]
  right  = [x for x in A if x > pivot]
  return quick_sort(left) + middle + quick_sort(right)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def selection_sort(A):
  """
  ----------------------------------------------------------------------------
  Sorts a list in-place using the Selection Sort algorithm.

  Parameters:
  - arr (list): The input list to be sorted.

  Returns:
  - list: The sorted list.

  Selection Sort divides the input list into a sorted and an unsorted region.
  It repeatedly selects the smallest element from the unsorted region and swaps it
  with the first element of the unsorted region.

  Example:
  >>> data = [4, 2, 7, 1, 9, 3]
  >>> selection_sort(data)
  [1, 2, 3, 4, 7, 9]

  Time Complexity:
  - Best Case: O(n^2) as it performs the same number of comparisons in all cases.
  - Worst Case: O(n^2).
  - Average Case: O(n^2).

  Space Complexity:
  - O(1) as it sorts the list in-place.
  """

  n = len(A)
  for i in range(n):
    min_index = i
    for j in range(i + 1, n):
      if A[j] < A[min_index]:
        min_index = j
    A[i], A[min_index] = A[min_index], A[i]