class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        array = [[words[i], len(words[i])] for i in range(len(words))]
        array.sort(key=lambda x: x[1])
        words = [array[i][0] for i in range(len(array))]
        res = []
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i] in words[j]:
                    res.append(words[i])
                    break
        return res