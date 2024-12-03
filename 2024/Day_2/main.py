
class Day2Solver:
    def __init__(self):
        pass

    def get_levels(self, lines):
        levels = []

        for line in lines:
            sanitized_line = line.strip().rstrip()
            levels.append(sanitized_line.split(' '))

        return levels

    def check_levels_as_safe(self, levels):
        safe = []

        for data_set in levels:
            increasing = False
            decreasing = False

            delta = int(data_set[0]) - int(data_set[1])
            if delta > 0:
                decreasing = True
            else:
                increasing = True

            failed = False
            j = 1
            for i in range(0, len(data_set) - 1):
                number_i = int(data_set[i])
                number_j = int(data_set[j])

                delta = int(data_set[i]) - int(data_set[j])
                if increasing:
                    if delta > 0:
                        failed = True
                    else:
                        if abs(delta) == 0:
                            failed = True
                        elif abs(delta) > 3:
                            failed = True
                elif decreasing:
                    if delta < 0:
                        failed = True
                    else:
                        if abs(delta) == 0:
                            failed = True
                        elif abs(delta) > 3:
                            failed = True
                j += 1

            if failed:
                safe.append(0)
            else:
                safe.append(1)

        return sum(safe)

    def create_all_data_set_combinations(self, single_level):
        all_combinations = []

        all_combinations.append(single_level) # keep the original so it can still be checked

        for i in range(0, len(single_level)):
            copy_of_list = list(single_level)
            copy_of_list.pop(i)
            all_combinations.append(copy_of_list)

        return all_combinations

    def check_levels_as_safe_with_dampener(self, levels):
        safe = []

        for data_set in levels:
            all_combinations = self.create_all_data_set_combinations(data_set)

            summed_safes = self.check_levels_as_safe(all_combinations)
            if summed_safes > 0:
                safe.append(1)
            else:
                safe.append(0)

        return sum(safe)

    def solve_part_1(self, in_file_name):
        f = open(in_file_name, 'r')
        lines = f.readlines()
        f.close()

        levels = self.get_levels(lines)
        num_safe = self.check_levels_as_safe(levels)
        print(f"{in_file_name}: num_safe: {num_safe}")

    def solve_part_2(self, in_file_name):
        f = open(in_file_name, 'r')
        lines = f.readlines()
        f.close()

        levels = self.get_levels(lines)
        num_safe = self.check_levels_as_safe_with_dampener(levels)
        print(f"{in_file_name}: num_safe: {num_safe}")


def main():
    '''
    Correct answers:

    input_simple_1.txt: num_safe: 2
    input.txt: num_safe: 510
    input_simple_1.txt: num_safe: 4
    input.txt: num_safe: 553
    '''

    day2Solver = Day2Solver()

    day2Solver.solve_part_1("input_simple_1.txt")
    day2Solver.solve_part_1("input.txt")

    day2Solver.solve_part_2("input_simple_1.txt")
    day2Solver.solve_part_2("input.txt")

if __name__ == "__main__":
    main()