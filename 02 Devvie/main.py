class Solution:

    def devvie(self, input):
        direction = 0
        x = 0
        y = 0
        x_vectors = [0, 1, 0, -1]
        y_vectors = [1, 0, -1, 0]
        for command in input:
            if command == 'L':
                direction = (direction - 1) % 4
            elif command == 'R':
                direction = (direction + 1) % 4
            elif command == 'F':
                x += x_vectors[direction]
                y += y_vectors[direction]
        if x == 0 and y == 0:
            return 0
        if x == 0:
            return abs(y) + (1 if y_vectors[direction] == 0 else 0) + (2 if y_vectors[direction] * y > 0 else 0)
        if y == 0:
            return abs(x) + (1 if x_vectors[direction] == 0 else 0) + (2 if x_vectors[direction] * x > 0 else 0)
        return abs(x) + abs(y) + (2 if x_vectors[direction] * x > 0 or y_vectors[direction] * y > 0 else 1)