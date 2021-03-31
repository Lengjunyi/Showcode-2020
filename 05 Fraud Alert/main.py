class PairValidator:

    def validate(self, input, input2):
        if len(input) != len(input2):
            return False
        if len(input) == 0:
            return False
        input = sorted([ord(i) for i in input])
        input2 = sorted([ord(i) for i in input2])
        for i in range(len(input)):
            if abs(input[i] - input2[i]) > 1:
                return False
        return True
