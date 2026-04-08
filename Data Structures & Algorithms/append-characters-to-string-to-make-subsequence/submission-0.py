class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        j = 0
        while i<len(s):
            if j==len(t):
                return 0
            if s[i]==t[j]:
                i+=1
                j+=1
            else:
                i+=1
        return len(t)-j