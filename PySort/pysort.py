"""
This module is a collection of sorting techniques
"""
class PySort():
    """
    This class contains the different sorting methods supported
    """
    SORTS = {
        "0": "merge_sort",
        "1": "bubble_sort",
        "2": "selection_sort",
        "3": "insertion_sort",
        "4": "shell_sort",
        "5": "quick_sort"
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

        if length == 0:
            return []

        elif length == 1:
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
        swap_index = None
        nums_length = len(nums)

        for i in range(nums_length-1):
            swap_index = i
            swap_element = nums[i]
            for j in range(i+1, nums_length):
                if nums[j] < swap_element:
                    swap_index = j
                    swap_element = nums[j]
            if i!= swap_index:
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

    def shell_sort(self, nums):
        """
        shell sort
        :param nums:
        :return:
        """
        def gap_insertion_sort(arr, start, gap):
            """
            gap insertion sort
            :param arr:
            :param start:
            :param gap:
            :return:
            """
            arr_length = len(arr)

            for index in range(start+gap, arr_length, gap):
                current_element = arr[index]
                position = index - gap
                while position >= 0 and current_element < arr[position]:
                    arr[position + gap] = arr[position]
                    position -= gap
                arr[position + gap] = current_element

            return arr

        sublist_length = len(nums) // 2

        while sublist_length > 0:
            for start in range(sublist_length):
                nums = gap_insertion_sort(nums, start, sublist_length)
            sublist_length //= 2

        return nums

    def quick_sort(self, nums):
        """
        quick sort
        :param nums:
        :return:
        """

        def partition(nums, start, end):
            pivot = (end + start) // 2
            left_mark = start
            right_mark = end

            pivot_value = nums[pivot]

            while True:
                while nums[left_mark] < pivot_value:
                    left_mark += 1
                while nums[right_mark] > pivot_value:
                    right_mark -= 1

                if left_mark >= right_mark:
                    return right_mark

                temp = nums[left_mark]
                nums[left_mark] = nums[right_mark]
                nums[right_mark] = temp

        def quick_sort_helper(nums, start, end):
            if start < end:
                p = partition(nums, start, end)
                quick_sort_helper(nums, start, p)
                quick_sort_helper(nums, p+1, end)

        start = 0
        end = len(nums) - 1
        quick_sort_helper(nums, start, end)

        return nums
