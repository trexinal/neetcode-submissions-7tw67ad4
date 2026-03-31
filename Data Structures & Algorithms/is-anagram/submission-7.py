class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sList = {}
        tList = {}

        for char in s:
            if char in sList:
                sList[char]+=1
            else: 
                sList[char] = 1
        

        for char in t:
            if char in tList:
                tList[char]+=1
            else: 
                tList[char] = 1

        return sList == tList

            
        