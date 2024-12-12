import two_sum


def test_twoSum1():
    nums = [2,7,9,15]
    target = 9
    assert [0,1] == two_sum.Solution().twoSum(nums, target)



def test_twoSum2():
    nums = [3,2,4]
    target = 6
    assert [1, 2] == two_sum.Solution().twoSum(nums, target)


def test_twoSum3():
    nums = [3,3]
    target = 6
    assert [0,1] == two_sum.Solution().twoSum(nums, target)