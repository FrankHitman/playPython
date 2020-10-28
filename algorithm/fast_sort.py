# /usr/bin/python


# code to implements quick sort thinking
def partition(a_list, min_idx, max_idx):
    x = a_list[max_idx]   # the last item
    print("the last_item is ", x)
    i = min_idx - 1  # why i begin with -1
    for j in range(min_idx, max_idx):
        if a_list[j] <= x:  # if the item
            i += 1
            a_list[i], a_list[j] = a_list[j], a_list[i]
            print a_list
    a_list[i + 1], a_list[max_idx] = a_list[max_idx], a_list[i + 1]
    print "------item < last_item will be put left; item > last_item will be put right-------"
    print a_list

    return i + 1


A = [2, 8, 7, 1, 3, 5, 6, 4]  # [7,4,5,2,1,6,3,2]


# print partition(A,0,7)
# print A

def quick_sort(a_list, min_idx, max_idx):
    print "min index is ", min_idx,"max index is ", max_idx
    if min_idx < max_idx:
        q = partition(a_list, min_idx, max_idx)
        print "get q is ", q
        quick_sort(a_list, min_idx, q - 1)

        quick_sort(a_list, q + 1, max_idx)


quick_sort(A, 0, len(A)-1)
