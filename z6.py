def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def main():
    try:
        numbers = [int(x) for x in input("Введите числа через пробел: ").split()]
        sorted_numbers = bubble_sort(numbers)
        print("Отсортированный список:", sorted_numbers)
    except ValueError:
        print("Введите только целые числа!")


if __name__ == "__main__":
    main()
