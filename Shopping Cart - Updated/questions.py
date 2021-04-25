# Given an array of integers, determine whether the array is monotonic or not.  (whether the numbers are in number order forwards or backwards)
A = [6, 5, 4, 4]
# Output:
# True

B = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
# Output:
# False
C = [1, 1, 2, 3, 7]
# Output:
# True

D = [1, 2, 3, 4]


def is_monotiic(some_list):
    index = 0
    aindex = 0
    for items in some_list[1:]:
        if items == some_list[index]:
            index += 1
        if items > some_list[index]:
            for items in some_list[1:]:
                if items >= some_list[aindex]:
                    aindex += 1
                    continue
                else:
                    return False
            return True

        if items < some_list[index]:
            for items in some_list[1:]:
                if items <= some_list[aindex]:
                    aindex += 1
                    continue
                else:
                    return False
            return True


print(is_monotiic(C))
