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

    def calculate_sides(self, plots):
        pass

    def calculate_area_perimter_price(self, garden_plots):
        price = 0
        for item in garden_plots:
            for plots in garden_plots[item]:
                area = self.calculate_area(plots)
                perimeter = self.calculate_perimeter(plots)
                price += (area * perimeter)
        
        return price

    def calculate_area_side_price(self, garden_plots):
        price = 0
        for item in garden_plots:
            for plots in garden_plots[item]:
                area = self.calculate_area(plots)
                sides = self.calculate_sides(plots)
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
        price = self.calculate_area_side_price(garden_plots)

        print(f"{in_file_name} price {price}")

def main():
    day12Solver = Day12Solver()

    day12Solver.solve_part_1("input_simple_1.txt")
    day12Solver.solve_part_1("input_simple_2.txt")
    day12Solver.solve_part_1("input.txt")

    day12Solver.solve_part_2("input_simple_1.txt")

if __name__ == "__main__":
    main()