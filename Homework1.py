def sorting(list):
    if len(list) <= 2:
        return list

    middle = len(list) // 2
    left = list[:middle]
    right = list[middle:]

    left = sorting(left)
    right = sorting(right)

    sorted_list = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            sorted_list.append(left[0])
            left.pop(0)
        else:
            sorted_list.append(right[0])
            right.pop(0)

    sorted_list += left
    sorted_list += right

    return sorted_list

