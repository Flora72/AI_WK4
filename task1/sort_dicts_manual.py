def sort_by_key_manual(data, key):
    sorted_list = []
    for item in data:
        sorted_list.append(item)
    sorted_list.sort(key=lambda x: x[key])
    return sorted_list
