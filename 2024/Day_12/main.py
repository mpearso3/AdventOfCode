class Day12Solver:
    def __init__(self):
        self.visited_locations = set()
        self.accounted_for_plot_locations = set()

    def initialize(self):
        self.visited_locations = set()
        self.accounted_for_plot_locations = set()

    def extract_garden(self, in_file_name):
        f = open(in_file_name, 'r')
        lines = f.readlines()
        f.close()

        garden = []

        for line in lines:
            sanitized_data = line.strip().rstrip()
            split_line = list(sanitized_data)

            garden.append(split_line)

        return garden

    def within_bounds(self, garden, row_i, col_i):
        if row_i < 0:
            return False
        if row_i >= len(garden):
            return False
        if col_i < 0:
            return False
        if col_i >= len(garden[0]):
            return False
        return True

    def walk_the_garden(self, connected_items, garden, row_i, col_i, item):
        if (row_i, col_i) in self.visited_locations:
            return
        
        if (row_i, col_i) in self.accounted_for_plot_locations:
            return

        if self.within_bounds(garden, row_i, col_i):
            self.visited_locations.add( (row_i, col_i) )
            compare_item = garden[row_i][col_i]

            if item == compare_item:
                connected_items.add( (row_i, col_i) )
                self.accounted_for_plot_locations.add( (row_i, col_i) )
            else:
                return
            
            self.walk_the_garden(connected_items, garden, row_i - 1, col_i    , item)
            self.walk_the_garden(connected_items, garden, row_i + 1, col_i    , item)
            self.walk_the_garden(connected_items, garden, row_i    , col_i - 1, item)
            self.walk_the_garden(connected_items, garden, row_i    , col_i + 1, item)

    def find_connected_items(self, garden, row_i, col_i, item):
        connected_items = set()
        self.walk_the_garden(connected_items, garden, row_i, col_i, item)
        return connected_items

    def extract_garden_plots(self, garden):
        garden_plots = dict()

        for row_i, row in enumerate(garden):
            for col_i, item in enumerate(row):

                self.visited_locations = set()

                if (row_i, col_i) in self.accounted_for_plot_locations:
                    continue

                connected_plots = self.find_connected_items(garden, row_i, col_i, item)

                # Only add if connected_plots is not empty
                if len(connected_plots) == 0:
                    connected_plots.add( (row_i, col_i) )

                if item not in garden_plots:
                    garden_plots[item] = []
                garden_plots[item].append(connected_plots)

        return garden_plots

    def calculate_area(self, plots):
        return len(plots)

    def calculate_perimeter(self, plots):
        perimeter = 0
        for plot in plots:
            r = plot[0]
            c = plot[1]

            if (r - 1, c    ) not in plots:
                perimeter += 1
            if (r + 1, c    ) not in plots:
                perimeter += 1
            if (r    , c - 1) not in plots:
                perimeter += 1
            if (r    , c + 1) not in plots:
                perimeter += 1

        return perimeter

    def get_direction_coordinates(self, direction, r, c):
        if direction == 'up':
            return (r - 1, c)
        elif direction == 'down':
            return (r + 1, c)
        elif direction == 'left':
            return (r, c - 1)
        elif direction == 'right':
            return (r, c + 1)

    def swap_row_and_column(self, plots):
        swap_x_and_y = list()
        for plot in plots:
            x = plot[0]
            y = plot[1]

            swap = (y, x)
            swap_x_and_y.append(swap)
        return swap_x_and_y

    def column_sorted(self, plots):
        swap_r_and_c = self.swap_row_and_column(plots)
        sorted_c = sorted(swap_r_and_c)
        swap_r_and_c = self.swap_row_and_column(sorted_c)
        return swap_r_and_c

    def check_continuous_coordinate(self, continuous, direction, previous, current):
        if direction == 'up' or direction == 'down':
            if previous != (current[0], current[1] - 1):
                continuous = False
        elif direction == 'right' or direction == 'left':
            if previous != (current[0] - 1, current[1]):
                continuous = False
        return continuous

    def find_sides(self, sorted_plots, sides, direction):
        num_sides = 0
        continuous = False
        
        previous_coordinate = None
        for plot in sorted_plots:
            r = plot[0]
            c = plot[1]

            coordinate = self.get_direction_coordinates(direction, r, c)
            if coordinate not in sorted_plots:
                continuous = self.check_continuous_coordinate(continuous, direction, previous_coordinate, plot)
                    
                if continuous == False:
                    continuous = True
                    sides.add((r, coordinate[0], coordinate[1], None))
                    num_sides += 1
            else:
                continuous = False

            previous_coordinate = plot

        # print(f"  {direction} sides: {num_sides}")
        return num_sides

    def calculate_sides(self, garden, plots, item):
        sides = set()
        num_sides = 0

        sorted_plots = sorted(plots)
        num_sides += self.find_sides(sorted_plots, sides, 'up'   )
        num_sides += self.find_sides(sorted_plots, sides, 'down' )

        sorted_plots = self.column_sorted(plots)
        num_sides += self.find_sides(sorted_plots, sides, 'right')
        num_sides += self.find_sides(sorted_plots, sides, 'left' )

        # print(f"{item}: sides: {len(sides)}")
        # print(f"{item}: num_sides: {num_sides}")
        return num_sides

    def calculate_area_perimter_price(self, garden_plots):
        price = 0
        for item in garden_plots:
            for plots in garden_plots[item]:
                area = self.calculate_area(plots)
                perimeter = self.calculate_perimeter(plots)
                price += (area * perimeter)
        
        return price

    def calculate_area_side_price(self, garden, garden_plots):
        price = 0
        for item in garden_plots:
            for plots in garden_plots[item]:
                area = self.calculate_area(plots)
                sides = self.calculate_sides(garden, plots, item)
                price += (area * sides)
        
        return price

    def solve_part_1(self, in_file_name):
        self.initialize()

        garden = self.extract_garden(in_file_name)

        garden_plots = self.extract_garden_plots(garden)
        price = self.calculate_area_perimter_price(garden_plots)

        print(f"{in_file_name} price {price}")

    def solve_part_2(self, in_file_name):
        self.initialize()

        garden = self.extract_garden(in_file_name)

        garden_plots = self.extract_garden_plots(garden)
        price = self.calculate_area_side_price(garden, garden_plots)

        print(f"{in_file_name} price {price}")

def main():
    day12Solver = Day12Solver()

    day12Solver.solve_part_1("input_simple_1.txt") # 140 expected
    day12Solver.solve_part_1("input_simple_2.txt") # 772 expected
    day12Solver.solve_part_1("input.txt")

    day12Solver.solve_part_2("input_simple_1.txt") # 80  expected
    day12Solver.solve_part_2("input_simple_2.txt") # 436 expected
    day12Solver.solve_part_2("input_simple_3.txt") # 236 expected
    day12Solver.solve_part_2("input_simple_4.txt") # 368 expected
    day12Solver.solve_part_2("input_simple_5.txt") # 1206 expected
    day12Solver.solve_part_2("input.txt")

if __name__ == "__main__":
    main()