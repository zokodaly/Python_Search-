def merge_sort(items):
   if len(items) <= 1:
       return items

    middle_index = len(items) // 2
    left_split = items[:middle_index]
    right_split = items[middle_index:]

    left_sorted = merge_sort(left_split)
    right_sorted = merge_sort(right_split)

   return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []

   while left and right:
       if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
       else:
            result.append(right[0])
            right.pop(0)

   if left:
        result += left
   if right:
        result += right

   return result


unordered_list = [356, 746, 264, 569, 949, 895, 125, 455, 787, 677, 391, 318, 543, 717, 180, 808,
                 113, 795, 19, 202, 534, 201, 370, 276, 975, 403, 624, 770, 595, 571, 268, 373]

ordered_list = merge_sort(unordered_list)

print(ordered_list)
#Output [19, 113, 125, 180, 201, 202, 264, 268, 276, 318, 356, 370, 373, 391, 403, 455, 534, 543, 569, 571, 595, 624, 677, 717, 746, 770, 787, 795, 808, 895, 949, 975]
