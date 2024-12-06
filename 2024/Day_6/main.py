class Day6Solver:
    def __init__(self):
        self.up    = 0
        self.right = 1
        self.down  = 2
        self.left  = 3

    def build_maze(self, lines):
        maze = []

        for line in lines:
            sanitized_line = line.strip().rstrip()
            maze.append(list(sanitized_line))

        return maze

    def is_guard(self, character):
        if character == '^':
            return True, self.up
        if character == '>':
            return True, self.right
        if character == '<':
            return True, self.down
        if character == 'v':
            return True, self.left
        return False,  -1

    def find_guard(self, maze):
        for row_i, row in enumerate(maze):
            for col_i, character in enumerate(row):

                is_guard, direction = self.is_guard(character)
                if is_guard:
                    return row_i, col_i, direction

        return -1, -1, -1

    def can_move(self, maze, guard_row, guard_col, direction):
        if direction == self.up:
            if guard_row > 0:
                if maze[guard_row - 1][guard_col] == "#":
                    return False, False
            else:
                return False, True

        if direction == self.right:
            if guard_col < (len(maze[guard_row]) - 1):
                if maze[guard_row][guard_col + 1] == "#":
                    return False, False
            else:
                return False, True
        
        if direction == self.down:
            if guard_row < (len(maze) - 1):
                if maze[guard_row + 1][guard_col] == "#":
                    return False, False
            else:
                return False, True

        if direction == self.left:
            if guard_col > 0:
                if maze[guard_row][guard_col - 1] == "#":
                    return False, False
            else:
                return False, True
        
        return True, False

    def move(self, guard_row, guard_col, direction):
        if direction == self.up:
            guard_row -= 1
        if direction == self.right:
            guard_col += 1
        if direction == self.down:
            guard_row += 1
        if direction == self.left:
            guard_col -= 1
        
        return guard_row, guard_col

    def rotate(self, direction):
        if direction == self.up:
            return self.right
        if direction == self.right:
            return self.down
        if direction == self.down:
            return self.left
        if direction == self.left:
            return self.up

    def print_maze(self, maze, guard_row, guard_col, direction):
        for row_i, row in enumerate(maze):
            row_string = ''
            for col_i, character in enumerate(row):
                if row_i == guard_row and col_i == guard_col:
                    if direction == self.up:
                        row_string = f"{row_string} ^"
                    if direction == self.right:
                        row_string = f"{row_string} >"
                    if direction == self.down:
                        row_string = f"{row_string} v"
                    if direction == self.left:
                        row_string = f"{row_string} <"
                else:
                    row_string = f"{row_string} {character}"
            print(row_string)
        print("")

    def walk_maze(self, maze, print_maze = False):
        guard_row, guard_col, direction = self.find_guard(maze)

        visited_locations = set()
        while (1):
            can_move, done = self.can_move(maze, guard_row, guard_col, direction)

            if done:
                break

            if can_move:
                guard_row, guard_col = self.move(guard_row, guard_col, direction)
                visited_locations.add((guard_row, guard_col))

                if print_maze:
                    self.print_maze(maze, guard_row, guard_col, direction)
            else:
                direction = self.rotate(direction)
        
        return len(visited_locations)

    def solve_part_1(self, in_file_name, print_maze):
        f = open(in_file_name, 'r')
        lines = f.readlines()
        f.close()

        maze = self.build_maze(lines)

        num_distinct_positions = self.walk_maze(maze, print_maze)
        print(f"{in_file_name} distinct positions {num_distinct_positions}")

    def solve_part_2(self, in_file_name):
        pass

def main():
    day6Solver = Day6Solver()

    day6Solver.solve_part_1("input_simple_1.txt", print_maze = True)
    day6Solver.solve_part_1("input.txt", print_maze = False)

    day6Solver.solve_part_2("input_simple_1.txt")

if __name__ == "__main__":
    main()