
nums = [10, 30, 40, 45, 70, 80, 85, 90, 100]
words = ["dog", "at", "good", "eye", "cat", "ball", "fish"]

elements = [39, 12, 18, 85, 72, 10, 2, 18]

# def linearSearch(anArray, search_item):
#     for item in anArray:
#         if item == search_item:
#
#             return anArray.index(item)
#
#     return -1
# print(linearSearch(elements, 4564))


# def binarySearch(anArray, item):
#     lower_index = 0
#     higher_index = len(anArray) - 1
#     while lower_index <= higher_index:
#         middle_index = ( lower_index + higher_index ) // 2
#         if item == anArray[middle_index]:
#             return middle_index
#         elif item < anArray[middle_index]:
#             higher_index = middle_index - 1
#         elif item > anArray[middle_index]:
#             lower_index = middle_index + 1
#     return -1
#
#
# print(binarySearch(nums, 10))

# elements = [39, 12, 18, 85, 72, 10, 2, 18]
#
#
# def bubbleSort(anArray):
#
#     for n in range(len(anArray) - 1):
#         for i in range(len(anArray) - n - 1):
#             if anArray[i] > anArray[i + 1]:
#                 anArray[i], anArray[i + 1] = anArray[i + 1], anArray[i]
#
#     return
#
#
# print("Unsorted list is,")
# print(elements)
# bubble(elements)
# print("Sorted Array is, ")
# print(elements)



# def selectionSort(anArray):
#     for slot in range(len(anArray)):
#         min_position = slot
#         for i in range(min_position, len(anArray)):
#             if anArray[i] < anArray[min_position]:
#                 min_position = i
#         (anArray[slot], anArray[min_position]) = (anArray[min_position], anArray[slot])
#
#
# print("Unsorted list is,")
# print(elements)
# selectionSort(elements)
# print("Sorted Array is, ")
# print(elements)


def insertionSort(anArray):
    for element in range(1, len(anArray)):


print("Unsorted list is,")
print(elements)
insertionSort(elements)
print("Sorted Array is, ")
print(elements)