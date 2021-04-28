# a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'


def wordcounter(some_str):
    string_list = some_str.replace(",", " ").lower().split()
    string_list.sort()
    word_count = {}
    for word in string_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


# print(wordcounter(a_text))


def linear_search(a_list, target):
    for i in range(len(a_list)):
        if a_list[i] == target:
            return i
    return -1


my_list = [5, 6, 7, 1, 8, 9]

print(linear_search(my_list, 9))
