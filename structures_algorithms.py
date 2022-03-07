# QUICKSORT
# %%
def quick_sort(sequence):  # take in a sequence of unsorted values
    length = len(sequence)
    if length <= 1:
        return sequence  # skip sequences that have a length of 0 or 1
    else:
        pivot = sequence.pop()  # remove and return last element

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    # apply algo to each items_lower, pivot in center, and apply algo again to items greater
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


print(quick_sort([3, 2, 4, 6, 5, 7, 6, 7, 7, 9, 3]))


# Two Sum-Leetcode 1
# nums = [2, 7, 11, 15], target = 9
# return index position [0,1] since sum is 9
# %%
