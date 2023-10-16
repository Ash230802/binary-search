from typing import List, Optional


def binary_search(sorted_collection: List[int], target: int) -> Optional[int]:
    """
    Perform binary search on a sorted collection.

    :param sorted_collection: A list of sorted numbers.
    :param target: The value to search for.
    :return: Index of the target value if found, else None.
    """
    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        midpoint = left + (right - left) // 2
        current_item = sorted_collection[midpoint]
        if current_item == target:
            return midpoint
        elif current_item < target:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return None


def insertion_sort(collection: List[int]) -> List[int]:
    """
    Perform insertion sort on a collection.

    :param collection: A list of numbers.
    :return: The sorted collection.
    """
    for i in range(1, len(collection)):
        current_item = collection[i]
        j = i - 1
        while j >= 0 and current_item < collection[j]:
            collection[j + 1] = collection[j]
            j -= 1
        collection[j + 1] = current_item
    return collection


def print_sorted_collection(collection: List[int]) -> None:
    """
    Print the sorted collection.

    :param collection: A list of numbers.
    """
    print(f"Sorted Collection: {', '.join(map(str, collection))}")


def binary_search_interface(input_list=None, target_value=None):
    print("Binary Search Program")
    print("----------------------")

    if input_list is None:
        user_input = input(
            "Enter numbers separated by spaces or commas (e.g., '1, 2, 3, 4, 5' or '1 2 3 4 5'): ").strip()
        # Replace commas with spaces and then split
        input_values = user_input.replace(',', '').rsplit()

        try:
            input_list = [int(item) for item in input_values]
        except ValueError:
            print(
                "Invalid input. Please enter valid integers separated by spaces or commas.")
            return

    if target_value is None:
        target_value = int(input("Enter a number to search for: "))

    print("Performing insertion sort...")
    sorted_collection = insertion_sort(input_list)
    print_sorted_collection(sorted_collection)

    result = binary_search(sorted_collection, target_value)

    if result is not None:
        print(f"{target_value} was found at index {result}.")
        return result
    else:
        print(f"{target_value} was not found in the collection.")
        return None


def main():
    binary_search_interface()

    while True:
        choice = input(
            "Do you want to perform another search? (yes/no): ").strip().lower()
        if choice != 'yes':
            break
        binary_search_interface()


if __name__ == "__main__":
    main()
