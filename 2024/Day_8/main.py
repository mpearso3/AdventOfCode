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

    def get_antinode_position(self, grid, row_1, row_2, col_1, col_2, row_delta, col_delta):
        temp_antinode_position_1 = []
        temp_antinode_position_2 = []

        if row_1 < row_2:
            temp_row = row_1 - row_delta
            if temp_row >= 0:
                temp_antinode_position_1.append(temp_row)

            temp_row = row_2 + row_delta
            if temp_row < len(grid):
                temp_antinode_position_2.append(temp_row)
        
        if row_1 > row_2:
            temp_row = row_1 + row_delta
            if temp_row < len(grid):
                temp_antinode_position_1.append(temp_row)

            temp_row = row_2 - row_delta
            if temp_row >= 0:
                temp_antinode_position_2.append(temp_row)

        if col_1 < col_2:
            temp_col = col_1 - col_delta
            if temp_col >= 0:
                temp_antinode_position_1.append(temp_col)

            temp_col = col_2 + col_delta
            if temp_col < len(grid[col_1]):
                temp_antinode_position_2.append(temp_col)
        
        if col_1 > col_2:
            temp_col = col_1 + col_delta
            if temp_col < len(grid[col_1]):
                temp_antinode_position_1.append(temp_col)

            temp_col = col_2 - col_delta
            if temp_col >= 0:
                temp_antinode_position_2.append(temp_col)

        antinode_position_1 = None
        antinode_position_2 = None

        if len(temp_antinode_position_1) > 1:
            antinode_position_1 = temp_antinode_position_1

        if len(temp_antinode_position_2) > 1:
            antinode_position_2 = temp_antinode_position_2

        return antinode_position_1, antinode_position_2

    def map_antinode_positions(self, grid, antennas):
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

                    antinode_position_1, antinode_position_2 = self.get_antinode_position(grid, row_1, row_2, col_1, col_2, row_delta, col_delta)
                    if antinode_position_1:
                        antinodes.add(tuple(antinode_position_1))
                    if antinode_position_2:
                        antinodes.add(tuple(antinode_position_2))

        return antinodes

    def solve_part_1(self, in_file_name):
        grid = self.create_grid(in_file_name)
        antennas = self.find_antenna_positions(grid)
        antinodes = self.map_antinode_positions(grid, antennas)

        print(f"{in_file_name} num antinodes {len(antinodes)}")

    def solve_part_2(self, in_file_name):
        pass

def main():
    day8Solver = Day8Solver()

    day8Solver.solve_part_1("input_simple_1.txt")
    day8Solver.solve_part_1("input.txt")

    day8Solver.solve_part_2("input_simple_1.txt")
    # day8Solver.solve_part_2("input.txt")

if __name__ == "__main__":
    main()