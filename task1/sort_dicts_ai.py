# Sort a list of dictionaries by a specific key
def sort_dicts_by_key(dicts, key):
    """
    Sorts a list of dictionaries by a specified key.

    Parameters:
    dicts (list): A list of dictionaries to be sorted.
    key (str): The key in the dictionaries to sort by.

    Returns:
    list: A new list of dictionaries sorted by the specified key.
    """
    return sorted(dicts, key=lambda x: x[key])
# Example usage
if __name__ == "__main__":  
    data = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35}
    ]
    sorted_data = sort_dicts_by_key(data, 'age')
    print(sorted_data)  # Output: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]
