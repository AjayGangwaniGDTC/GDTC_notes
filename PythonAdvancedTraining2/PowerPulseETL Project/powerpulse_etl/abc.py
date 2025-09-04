def isArraySpecial(nums):
    def parity(num):
        print(num)
        if num % 2 == 0:
            return 'even'
        return 'odd'


    for i in range(1, len(nums)):
        if parity(nums[i]) == parity(nums[i - 1]):
            return False
    return True


isArraySpecial([2, 1, 4])