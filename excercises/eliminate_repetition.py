def remove_duplicates(a_list):
    for each in a_list:
        if a_list.count(each) > 1:
            a_list.remove(each)
    return a_list


print(remove_duplicates([2, 2, 3, "hi", 3, 3, 9, 9, "hi", True, True, [1, 1]]))