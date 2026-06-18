def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Main program
print("DAA LAB PROGRAM (Python)")
n = int(input("Enter number of elements: "))

arr = []
print("Enter elements:")
for i in range(n):
    arr.append(int(input()))

while True:
    print("\n----- MENU -----")
    print("1. Bubble Sort")
    print("2. Linear Search")
    print("3. Binary Search")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Sorted array:", bubble_sort(arr.copy()))

    elif choice == 2:
        key = int(input("Enter element to search: "))
        result = linear_search(arr, key)
        if result != -1:
            print("Element found at index", result)
        else:
            print("Not found")

    elif choice == 3:
        key = int(input("Enter element to search (array must be sorted): "))
        sorted_arr = bubble_sort(arr.copy())
        result = binary_search(sorted_arr, key)

        if result != -1:
            print("Element found at index", result)
        else:
            print("Not found")

    elif choice == 4:
        print("Exit...")
        break

    else:
        print("Invalid choice")