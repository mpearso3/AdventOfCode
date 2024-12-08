class Day8Solver:
    def create_grid(self, in_file_name):
        f = open(in_file_name, 'r')
        lines = f.readlines()
        f.close()

        grid = []
        for line in lines:
            sanitized_line = line.strip().rstrip()
            grid.append(list(sanitized_line))

        return grid

    def find_antenna_positions(self, grid):
        antennas = {}

        for row_i, row in enumerate(grid):
            for col_i, col in enumerate(row):
                character = grid[row_i][col_i]

                if character.isdigit() or character.isalpha():
                    if character not in antennas:
                        antennas[character] = []
                    antennas[character].append([row_i, col_i])

        return antennas

    def get_antinode_position(self, pos_1, pos_2, pos_delta):
        pos_antinode_position_1 = None
        pos_antinode_position_2 = None

        if pos_1 < pos_2:
            pos_antinode_position_1 = pos_1 - pos_delta
            pos_antinode_position_2 = pos_2 + pos_delta
        
        if pos_1 > pos_2:
            pos_antinode_position_1 = pos_1 + pos_delta
            pos_antinode_position_2 = pos_2 - pos_delta

        return pos_antinode_position_1, pos_antinode_position_2

    def map_antinode_positions(self, antennas):
        antinodes = set()

        row = 0
        col = 1

        for antenna in antennas:
            for i in range(0, len(antennas[antenna])):
                position_1 = antennas[antenna][i]
                row_1 = position_1[row]
                col_1 = position_1[col]

                for j in range(i + 1, len(antennas[antenna])):
                    position_2 = antennas[antenna][j]
                    row_2 = position_2[row]
                    col_2 = position_2[col]

                    row_delta = abs(row_1 - row_2)
                    col_delta = abs(col_1 - col_2)

                    antinode_row_1, antinode_row_2 = self.get_antinode_position(row_1, row_2, row_delta)
                    antinode_col_1, antinode_col_2 = self.get_antinode_position(col_1, col_2, col_delta)

                    antinodes.add((antinode_row_1, antinode_col_1))
                    antinodes.add((antinode_row_2, antinode_col_2))

        return antinodes

    def max_harmonics(self, num_rows, row_delta, num_cols, col_delta):
        row_harmonics = int(num_rows / row_delta)
        col_harmonics = int(num_cols / col_delta)

        return max(row_harmonics, col_harmonics) + 100

    def map_antinode_harmonic_positions(self, grid, antennas):
        antinodes = set()

        row = 0
        col = 1

        num_rows = len(grid)
        num_cols = len(grid[0])

        for antenna in antennas:
            for i in range(0, len(antennas[antenna])):
                position_1 = antennas[antenna][i]
                row_1 = position_1[row]
                col_1 = position_1[col]

                for j in range(i + 1, len(antennas[antenna])):
                    position_2 = antennas[antenna][j]
                    row_2 = position_2[row]
                    col_2 = position_2[col]

                    row_delta = abs(row_1 - row_2)
                    col_delta = abs(col_1 - col_2)

                    max_harmonic = self.max_harmonics(num_rows, row_delta, num_cols, col_delta)

                    antinode_row_1, antinode_row_2 = self.get_antinode_position(row_1, row_2, row_delta)
                    antinode_col_1, antinode_col_2 = self.get_antinode_position(col_1, col_2, col_delta)
                    antinodes.add((antinode_row_1, antinode_col_1))
                    antinodes.add((antinode_row_2, antinode_col_2))

                    previous_row_1 = row_1
                    current_row_1 = antinode_row_1
                    previous_col_1 = col_1
                    current_col_1 = antinode_col_1
                    for i in range(max_harmonic):
                        harmonic_antinode_row_1, harmonic_antinode_row_2 = self.get_antinode_position(current_row_1, previous_row_1, row_delta)
                        harmonic_antinode_col_1, harmonic_antinode_col_2 = self.get_antinode_position(current_col_1, previous_col_1, col_delta)
                        antinodes.add((harmonic_antinode_row_1, harmonic_antinode_col_1))

                        previous_row_1 = current_row_1
                        current_row_1 = harmonic_antinode_row_1
                        previous_col_1 = current_col_1
                        current_col_1 = harmonic_antinode_col_1

                    previous_row_1 = row_2
                    current_row_1 = antinode_row_2
                    previous_col_1 = col_2
                    current_col_1 = antinode_col_2
                    for i in range(max_harmonic):
                        harmonic_antinode_row_1, harmonic_antinode_row_2 = self.get_antinode_position(current_row_1, previous_row_1, row_delta)
                        harmonic_antinode_col_1, harmonic_antinode_col_2 = self.get_antinode_position(current_col_1, previous_col_1, col_delta)
                        antinodes.add((harmonic_antinode_row_1, harmonic_antinode_col_1))

                        previous_row_1 = current_row_1
                        current_row_1 = harmonic_antinode_row_1
                        previous_col_1 = current_col_1
                        current_col_1 = harmonic_antinode_col_1

                    previous_row_2 = row_2
                    current_row_2 = antinode_row_2
                    previous_col_2 = col_2
                    current_col_2 = antinode_col_2
                    for i in range(max_harmonic):
                        harmonic_antinode_row_1, harmonic_antinode_row_2 = self.get_antinode_position(current_row_2, previous_row_2, row_delta)
                        harmonic_antinode_col_1, harmonic_antinode_col_2 = self.get_antinode_position(current_col_2, previous_col_2, col_delta)
                        antinodes.add((harmonic_antinode_row_2, harmonic_antinode_col_2))

                        previous_row_2 = current_row_2
                        current_row_2 = harmonic_antinode_row_2
                        previous_col_2 = current_col_2
                        current_col_2 = harmonic_antinode_col_2

                    previous_row_2 = row_1
                    current_row_2 = antinode_row_1
                    previous_col_2 = col_1
                    current_col_2 = antinode_col_1
                    for i in range(max_harmonic):
                        harmonic_antinode_row_1, harmonic_antinode_row_2 = self.get_antinode_position(current_row_2, previous_row_2, row_delta)
                        harmonic_antinode_col_1, harmonic_antinode_col_2 = self.get_antinode_position(current_col_2, previous_col_2, col_delta)
                        antinodes.add((harmonic_antinode_row_2, harmonic_antinode_col_2))

                        previous_row_2 = current_row_2
                        current_row_2 = harmonic_antinode_row_2
                        previous_col_2 = current_col_2
                        current_col_2 = harmonic_antinode_col_2

        return antinodes

    def prune_false_antinode_positions(self, grid, antinodes):
        valid_antinodes = set()

        num_rows = len(grid)
        num_cols = len(grid[0])

        for antinode in antinodes:
            row = antinode[0]
            col = antinode[1]

            if row >= 0 and row < num_rows:
                if col >= 0 and col < num_cols:
                    valid_antinodes.add(antinode)

        return valid_antinodes

    def print_grid_with_antinodes(self, grid, antinodes):
        for row_i, row in enumerate(grid):
            row_string = ''
            for col_i, col in enumerate(row):
                character = grid[row_i][col_i]

                if (row_i, col_i) in antinodes:
                    row_string += '#'
                else:
                    row_string += character
            print(f"{row_string}")

    def solve_part_1(self, in_file_name):
        grid = self.create_grid(in_file_name)
        antennas = self.find_antenna_positions(grid)

        antinodes = self.map_antinode_positions(antennas)
        antinodes = self.prune_false_antinode_positions(grid, antinodes)

        print(f"{in_file_name} num antinodes {len(antinodes)}")

    def solve_part_2(self, in_file_name):
        grid = self.create_grid(in_file_name)
        antennas = self.find_antenna_positions(grid)

        antinodes = self.map_antinode_harmonic_positions(grid, antennas)
        antinodes = self.prune_false_antinode_positions(grid, antinodes)

        self.print_grid_with_antinodes(grid, antinodes)

        print(f"{in_file_name} num antinodes {len(antinodes)}")

def main():
    day8Solver = Day8Solver()

    day8Solver.solve_part_1("input_simple_1.txt")
    day8Solver.solve_part_1("input.txt")

    day8Solver.solve_part_2("input_simple_1.txt")
    day8Solver.solve_part_2("input.txt")

if __name__ == "__main__":
    main()