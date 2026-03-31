class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {} # map of chars
        l = 0 #length
        res = 0 # whtat the max length seen is 

        for r in range(len(s)):
            if s[r] in mp: # if char is already in map
                l = max(mp[s[r]] + 1, l) 
            mp[s[r]] = r
            res = max(res, r-l+1)
        return res
            