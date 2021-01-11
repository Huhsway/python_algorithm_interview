# 풀이 3 파이썬 다운 방식
def arrayPairSum(self, nums: List[int]) -> int:
    return sum(sorted(nums)[::2])