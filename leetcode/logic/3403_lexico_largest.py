class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        """
        Largest string will be of size `len(word)-num_friends+1`
        """
        if numFriends == 1:
            return word
        n = len(word)
        m = n - numFriends + 1
        return max(word[i : i + m] for i in range(n))


s = Solution()
string = "cgwzebexlahnfqsetbeaybmfdzywpvehjybpwiotnciddjonfi"
res = s.answerString(string, 21)
print(res)
