#A list is needed 
myList = [1, 5, 7, 3, 9, 8, 6, 4, 2]


def bubble_sort(arr):

    iteration_count = 0
   for i in range(len(arr)):
       for x in range(len(arr) - i - 1):
            iteration_count += 1

           # Swap if necessary
           if arr[x] > arr[x + 1]:
                arr[x], arr[x + 1] = arr[x + 1], arr[x]


if __name__ == "__main__":

    bubble_sort(myList)
   print(myList)

>>> [1, 2, 3, 4, 5, 6, 7, 8, 9]
