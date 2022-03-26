class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slist = list(s)
        ans = 0
        for i in range(len(slist)):
            c = 1
            v = {slist[i]: 1}
            for j in range(i+1, len(slist)):
                if slist[j] not in v:
                    v[slist[j]] = 1
                    c += 1
                else:
                    break
            ans = max(ans, c)
        return ans
