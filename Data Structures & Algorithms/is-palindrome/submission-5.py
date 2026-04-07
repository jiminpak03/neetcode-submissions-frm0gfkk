class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = list(s.lower())
        l, r = 0, len(arr) - 1
        while l <= r:
            if not arr[l].isalnum():
                l += 1
            elif not arr[r].isalnum():
                r -= 1
            elif arr[l] != arr[r]:
                return False
            else:
                l += 1
                r -= 1
        return True