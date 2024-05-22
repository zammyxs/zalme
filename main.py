from countingsort import countingsort
from radixsort import radixsort
from insertsort import insertsort
from quicksort import quicksort


def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

def print_menu():
    print("Choose a sorting algorithm:")
    print("1. Radix Sort")
    print("2. Counting Sort")
    print("3. Insertion Sort")
    print("4. Quick Sort")

def main():
    user_input = input("Enter the numbers to sort: ")
    data = list(map(int, user_input.split()))
    print("Original data:", data)

    print_menu()
    choice = input("Choose a number: ")

    if choice == '1':
        print("Sorting using Radix Sort:")
        sorted_data = radix_sort(data[:])
    elif choice == '2':
        print("Sorting using Counting Sort:")
        sorted_data = counting_sort(data[:])
    elif choice == '3':
        print("Sorting using Insertion Sort:")
        sorted_data = insertion_sort(data[:])
    elif choice == '4':
        print("Sorting using Quick Sort:")
        sorted_data = quick_sort(data[:])
    else:
        print("Invalid choice. Please select a valid option.")
        return

    print("Sorted data:", sorted_data)

if __name__ == "__main__":
    main()
