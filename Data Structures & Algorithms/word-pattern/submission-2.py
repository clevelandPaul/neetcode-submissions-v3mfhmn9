class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_lst = s.split(' ')
        if len(pattern)!=len(s_lst):
            return False
        pattern_dict = {}
        s_dict = {}
        for i in range(len(pattern)):
            if pattern[i] in pattern_dict:
                if pattern_dict[pattern[i]]!=s_lst[i]:
                    return False
            if s_lst[i] in s_dict:
                if s_dict[s_lst[i]]!=pattern[i]:
                    return False
            pattern_dict[pattern[i]] = s_lst[i]
            s_dict[s_lst[i]] = pattern[i]

        return True
        
        