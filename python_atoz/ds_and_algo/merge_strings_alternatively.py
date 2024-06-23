class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_w1 = len(word1)
        len_w2 = len(word2)
        result = []
        i = j = 0
        while i < min(len_w1, len_w2) and j < min(len_w1, len_w2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1
            print(result)
        while i < len_w1:
            result.append(word1[i])
            i += 1
            print(result)
        while j < len_w2:
            result.append(word2[j])
            j += 1
            print(result)

        return "".join(result)


if __name__ == '__main__':
    result = Solution().mergeAlternately("abc", "pqr")
    print(result)
