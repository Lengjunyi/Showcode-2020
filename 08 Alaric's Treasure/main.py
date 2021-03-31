class Solution:

    def parse_roman_numerals(self, input):
        conversion_table = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        values = [conversion_table[i] for i in input]
        for i in range(len(values)-1):
            if values[i] < values[i+1]:
                values[i] *= -1
        return sum(values)
