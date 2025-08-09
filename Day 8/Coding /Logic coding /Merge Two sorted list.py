"""Merge Two Sorted Lists

Explanation:
Two sorted lists can be merged using sorted() after combining.
"""
def merge_sorted_lists(l1, l2):
    return sorted(l1 + l2)

print(merge_sorted_lists([1,3,5], [2,4,6]))  # [1,2,3,4,5,6]

#Sample Output:[1, 2, 3, 4, 5, 6]
