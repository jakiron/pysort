"""
This module is a collection of sorting techniques
"""
class Sort():
    """
    This class contains the different sorting methods supported
    """
    SORTS = {
        "0": "merge_sort",
        "1": "bubble_sort",
        "2": "selection_sort",
        "3": "insertion_sort"
    }

    def __init__(self, sort_type=0):
        """

        :param sort_type:
        """
        self._sort_type = str(sort_type)

    def sort(self, nums):
        """

        :param nums:
        :return:
        """
        def default_func(func_name):
            print("Method: %s not found"%(func_name))
        return getattr(self, self.SORTS[self._sort_type], default_func)(nums)

    def merge_sort(self, nums):
        """
        merge sort

        :param nums:
        :return:
        """
        sorted_nums = []
        length = len(nums)

        if length == 1:
            return nums

        mid_point = length // 2
        arr1 = self.merge_sort(nums[:mid_point])
        arr2 = self.merge_sort(nums[mid_point:])

        arr1_length = len(arr1)
        arr2_length = len(arr2)

        arr1_pointer = 0
        arr2_pointer = 0

        while (arr1_pointer < arr1_length and arr2_pointer < arr2_length):
            if arr1[arr1_pointer] <  arr2[arr2_pointer]:
                sorted_nums.append(arr1[arr1_pointer])
                arr1_pointer+=1
            elif arr2[arr2_pointer] < arr1[arr1_pointer]:
                sorted_nums.append(arr2[arr2_pointer])
                arr2_pointer+=1
        if arr1_pointer < arr1_length:
            sorted_nums.extend(arr1[arr1_pointer:])
        elif arr2_pointer < arr2_length:
            sorted_nums.extend(arr2[arr2_pointer:])
        return sorted_nums

    def bubble_sort(self, nums):
        """
        bubble sort

        :param nums:
        :return:
        """
        swap = None
        nums_length = len(nums)

        while(swap != 0):
            swap = 0
            index = 1
            while index < nums_length:
                if nums[index - 1] > nums[index]:
                    nums[index - 1], nums[index] = nums[index], nums[index-1]
                    swap += 1
                index += 1
            nums_length -= 1
        return nums

    def selection_sort(self, nums):
        """
        selection sort
        :param nums:
        :return:
        """
        swap_element = None
        swap_index = None
        nums_length = len(nums)

        for i in range(nums_length-1):
            swap_index = i
            swap_element = nums[swap_index]
            for j in range(i, nums_length):
                if nums[j] < swap_element:
                    swap_index = j
            swap_element = nums[swap_index]
            nums[swap_index] = nums[i]
            nums[i] = swap_element

        return nums

    def insertion_sort(self, nums):
        """
        insertion sort
        :param nums:
        :return:
        """
        nums_length = len(nums)
        for i in range(1, nums_length):
            current_element = nums[i]
            j = i - 1
            while j >= 0 and (current_element < nums[j]):
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = current_element

        return nums
