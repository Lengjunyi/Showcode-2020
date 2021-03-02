class AttackCleanup:

    def restore_data(self, message):
        import re
        combinations = re.findall("[0-9]*[a-z]", message)
        raw_result = "".join(c if len(c) == 1 else c[-1] * int(c[:-1]) for c in combinations)
        result = ""
        for i in raw_result:
            result += chr(ord('a') + ord('z') - ord(i))
        return result