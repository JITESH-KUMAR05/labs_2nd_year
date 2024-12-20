class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        self.s = sentence.split()
        self.w = searchWord
        for i in range(len(self.s)):
            # print(len(self.s))
            # if self.w in self.s[i]:
            #     return i + 1
            if self.s.startswith(self.w):
                return  i + 1
        return -1

m = Solution()

