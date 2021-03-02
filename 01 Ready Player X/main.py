class Cipher:

    def halliday(self, message):
        ans = ""
        for i in message:
            if ord(i) >= ord('a') and ord(i) <= ord('z'):
                ans += chr((ord(i) - ord('a') + 13) % 26 + ord('a'))
            elif ord(i) >= ord('A') and ord(i) <= ord('Z'):
                ans += chr((ord(i) - ord('A') + 13) % 26 + ord('A'))
            else:
                ans += i
        return ans