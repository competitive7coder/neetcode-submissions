class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        start, end = 0, len(people) - 1
        total_weight, boats = 0, 0
        while start <= end: # <= for single element 
            total_weight = people[start] + people[end]
            if total_weight <= limit:
                start += 1
                end -= 1
                boats += 1
            else:
                end  -= 1
                boats += 1
        return boats

