class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)
        ans = float('inf')
        def canFinish(arr):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / arr)
            if hours <= h:
                return hours
        while start <= end:
            mid = start + (end - start) // 2
            if canFinish(mid):
                ans = mid
                end = mid - 1
            else:
                start = mid + 1
        return ans