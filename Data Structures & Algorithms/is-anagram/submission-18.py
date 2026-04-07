class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        bank = {}
        for ch in s:
            bank[ch] = bank.get(ch, 0) + 1

        for ch in t:
            if ch not in bank or bank[ch] == 0:
                return False
            bank[ch] -= 1

        return True
