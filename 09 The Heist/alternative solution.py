class Solution:

    def calculate_capacity(self, input):
        ans = 0
        for i in range(256):
            first = -1
            last = -1
            for j in range(len(input)):
                if input[j] >= i:
                    first = j
                    break
            for j in range(len(input)):
                if input[j] >= i:
                    last = j
            for j in range(first, last):
                if input[j] < i:
                    ans += 1
        return ans
