class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) -1 
        while left <= right:
            mid = left + (right - left) // 2
            if ord(letters[mid]) > ord(target):
                if mid == 0 or ord(letters[mid - 1]) <= ord(target):
                    return letters[mid]
                else:
                    right = mid -1
            elif ord(letters[mid]) <= ord(target):
                left = mid + 1
        return letters[0]