class Solution:

    def get_recipient(self, message, position):
        import re
        names = re.findall("@[a-zA-Z0-9\-\_]+", message)
        if (position <= len(names)):
            return names[position - 1][1:]
        return ""