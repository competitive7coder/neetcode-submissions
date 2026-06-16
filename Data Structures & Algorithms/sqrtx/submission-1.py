class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 0, x
        res = 0
        while start <= end:
            mid = start + (end - start) // 2
            if mid * mid == x:
                res = mid
                return res
            elif mid * mid > x:
                end = mid - 1
            else:
                res = mid
                start = mid + 1
                
        return res