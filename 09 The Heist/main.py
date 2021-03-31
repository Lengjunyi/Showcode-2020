class Solution:

    def calculate_capacity(self, input):
        highest_from_left = [i for i in input]
        highest_from_right = [i for i in input]
        length = len(input)
        for i in range(1, length):
            highest_from_left[i] = max(highest_from_left[i], highest_from_left[i-1])
            highest_from_right[length-i-1] = max(highest_from_right[length-i-1], highest_from_right[length-i])
        ans = 0
        for i in range(length):
            ans += max(0, min(highest_from_left[i], highest_from_right[i]) - input[i])
        return ans
