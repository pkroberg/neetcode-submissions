class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if length != same -> false
        # create 2 hashmaps {letter : number of occurances}
        # if 2 hashmaps are not the same -> false
        # otherwise true

        if len(s) != len(t):
            return False

        mapS, mapT = {}, {}

        for i in range(len(s)):
            mapS[s[i]] = 1 + mapS.get(s[i], 0)
            mapT[t[i]] = 1 + mapT.get(t[i], 0)
        
        if mapS == mapT:
            return True

        return False
