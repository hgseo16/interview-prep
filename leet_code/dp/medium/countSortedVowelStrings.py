class Solution(object):
    def countVowelStrings(self, n):

        def rec(n, k):
            if n == 0:
                return 1

            total = 0

            for i in range(k, 5):
                total += rec(n - 1, i)

            return total

        return rec(n, 0)