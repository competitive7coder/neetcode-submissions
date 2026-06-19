class Solution:
    def reverseString(self, s: List[str]) -> None:
        # Revising Two Pointers Pattern
        start, end = 0, len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
