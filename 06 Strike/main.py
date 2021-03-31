class Solution:

    def get_score(self, input):
        points = []
        for i in input:
            if i == 'X':
                points.append(10)
            elif i == '/':
                points.append(10 - points[-1])
            else:
                points.append(int(i))
        if input[-1] == '/':
            points[-1] -= points[-3]
        points += [0, 0]
        frame = 0
        for i in range(len(input)):
            if frame == 9:
                break
            if input[i] == 'X':
                points[i] += points[i+1] + points[i+2]
                frame += 0.5
            elif input[i] == '/':
                points[i] += points[i+1]
            frame += 0.5
        return sum(points)
