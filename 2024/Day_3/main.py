import re

class Day3Solver:
    def extract_valid_multiply_statements(self, pairs, line):
        pattern = "mul\((\d+),(\d+)\)"

        matches = re.findall(pattern, line, re.IGNORECASE)

        for match in matches:
            pairs.append(match)

    def multiply_and_sum_pairs(self, pairs):
        sum = 0

        for pair in pairs:
            num_1 = int(pair[0])
            num_2 = int(pair[1])

            sum += (num_1 * num_2)

        return sum

    def solve_part_1(self, in_file_name):
        f = open(in_file_name, 'r')
        lines = f.readlines()
        f.close()

        pairs = []
        for line in lines:
            self.extract_valid_multiply_statements(pairs, line)

        multiplies = self.multiply_and_sum_pairs(pairs)
        print(f"{in_file_name}: sum: {multiplies}")

    def get_pattern_indexes(self, pattern, input):
        matches = []
        for match in re.finditer(pattern, input):
            matches.append(match.start())
        return matches

    def remove_invalid_pairs(self, dont_matches, do_matches, mul_matches):
        valid_indexes = []

        current_dont_index = dont_matches.pop(0)
        current_do_index = do_matches.pop(0)

        enabled = True
        for i, index in enumerate(mul_matches):
            if index < current_do_index and index < current_dont_index:
                if enabled:
                    valid_indexes.append(i)
            elif index > current_do_index and index < current_dont_index:
                enabled = True
                valid_indexes.append(i)
                if len(do_matches) > 0:
                    current_do_index = do_matches.pop(0)            
            elif index > current_dont_index and index < current_do_index:
                enabled = False
                if len(dont_matches) > 0:
                    current_dont_index = dont_matches.pop(0)            
            else: # greater than both
                if current_dont_index > current_do_index:
                    enabled = False
                else:
                    enabled = True
                    valid_indexes.append(i)

                if len(dont_matches) > 0:
                    current_dont_index = dont_matches.pop(0)            
                if len(do_matches) > 0:
                    current_do_index = do_matches.pop(0)            

        return valid_indexes

    def solve_part_2(self, in_file_name):
        f = open(in_file_name, 'r')
        lines = f.readlines()
        f.close()

        full_input = ''
        for line in lines:
            sanitized_line = line.strip().rstrip()
            full_input += sanitized_line

        dont_matches = self.get_pattern_indexes("don't\(\)", full_input)
        do_matches = self.get_pattern_indexes("do\(\)", full_input)
        mul_matches = self.get_pattern_indexes("mul\((\d+),(\d+)\)", full_input)

        multiply_pairs = []
        self.extract_valid_multiply_statements(multiply_pairs, full_input)

        valid_multiply_pairs = self.remove_invalid_pairs(dont_matches, do_matches, mul_matches)

        pairs = []
        for i in valid_multiply_pairs:
            pairs.append(multiply_pairs[i])

        multiplies = self.multiply_and_sum_pairs(pairs)
        print(f"{in_file_name}: sum: {multiplies}")

def main():
    day3Solver = Day3Solver()

    day3Solver.solve_part_1("input_simple_1.txt")
    day3Solver.solve_part_1("input.txt")

    day3Solver.solve_part_2("input_simple_2.txt")
    day3Solver.solve_part_2("input_simple_3.txt")
    day3Solver.solve_part_2("input.txt")

if __name__ == "__main__":
    main()