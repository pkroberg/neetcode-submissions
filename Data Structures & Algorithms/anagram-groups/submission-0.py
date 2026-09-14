class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countList = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for l in s:
                count[ord(l) - ord("a")] += 1

            countList[tuple(count)].append(s)

        return list(countList.values())