class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_dict = {}
        for c in chars:
            char_dict[c] = char_dict.get(c, 0)+1
        res_len = 0
        for i in range(len(words)):
            word_dict = {}
            bFlag = True
            for j in range(len(words[i])):
                if words[i][j] not in char_dict:
                    bFlag = False
                    break
                else:
                    word_dict[words[i][j]] = word_dict.get(words[i][j], 0)+1
                    if word_dict[words[i][j]]>char_dict[words[i][j]]:
                        bFlag = False
                        break
            if bFlag:
                res_len += len(words[i])
        return res_len