class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store = set()
        for num in nums:
            if num not in store:
                store.add(num)
            else:
                return True
        return False