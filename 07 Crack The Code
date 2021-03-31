class Solution:

    def cipher(self, input, key):
        ans = ""
        for i in input:
            if 'A' <= i <= 'Z':
                ans += chr(ord('A') + (ord(i) - ord('A') + key) % 26)
            elif 'a' <= i <= 'z':
                ans += chr(ord('a') + (ord(i) - ord('a') + key) % 26)
            else:
                ans += i
        return ans
