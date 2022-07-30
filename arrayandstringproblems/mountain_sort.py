
# runtime o(nlogn)
def mountain_sort(nums):

    sorted_nums = sorted(nums)

    for i in range(1, len(sorted_nums) - 2, 2):
        sorted_nums[i], sorted_nums[i+1] = sorted_nums[i + 1], sorted_nums[i]
        # print(i)
    return sorted_nums


def test_mountain_sort(nums):
    for i in range(1, len(nums) - 1):
        if i % 2 == 1:
            if not (nums[i - 1] <= nums[i] >= nums[i + 1]):
                print("failed")
        else:
            if not (nums[i - 1] >= nums[i] <= nums[i + 1]):
                print("failed")
    print("passed")


def test():
    test_mountain_sort(mountain_sort([1, 3, 2, 5, 2, 1, 7, 9]))



if __name__ == "__main__":
    test()