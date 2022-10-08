def list_extension(*lists):
    new_list = []
    for list in lists:
        new_list += list
    return new_list

print(list_extension([1, 2, 3], [3, 100, 5.42], [6, 7, 8]))