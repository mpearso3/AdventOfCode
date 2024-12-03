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
        matches = {}
        for match in re.finditer(pattern, input):
            start_index = match.start()
            matches[start_index] = pattern
        return matches

    def remove_invalid_pairs(self, sorted_matches):
        valid_indexes = []

        mul_count = 0
        enabled = True
        for start_index, pattern in sorted_matches.items():
            if 'mul' in pattern:
                if enabled:
                    valid_indexes.append(mul_count)
                mul_count += 1
            elif "don't" in pattern:
                enabled = False
            elif 'do' in pattern:
                enabled = True

        return valid_indexes

    def get_input_as_single_string(self, in_file_name):
        f = open(in_file_name, 'r')
        lines = f.readlines()
        f.close()

        full_input = ''
        for line in lines:
            sanitized_line = line.strip().rstrip()
            full_input += sanitized_line
        
        return full_input

    def combine_matches(self, dont_matches, do_matches, mul_matches):
        matches = {}
        matches.update(dont_matches)
        matches.update(do_matches)
        matches.update(mul_matches)

        sorted_matches = dict(sorted(matches.items()))

        return sorted_matches

    def solve_part_2(self, in_file_name):
        full_input = self.get_input_as_single_string(in_file_name)

        dont_matches = self.get_pattern_indexes("don't\(\)", full_input)
        do_matches = self.get_pattern_indexes("do\(\)", full_input)
        mul_matches = self.get_pattern_indexes("mul\((\d+),(\d+)\)", full_input)

        sorted_matches = self.combine_matches(dont_matches, do_matches, mul_matches)
        valid_multiply_pairs = self.remove_invalid_pairs(sorted_matches)

        multiply_pairs = []
        self.extract_valid_multiply_statements(multiply_pairs, full_input)

        pairs = []
        for i in valid_multiply_pairs:
            pairs.append(multiply_pairs[i])

        multiplies = self.multiply_and_sum_pairs(pairs)
        print(f"{in_file_name}: sum: {multiplies}")

def main():
    '''
    Correct answers to files:

    input_simple_1.txt: sum: 161
    input.txt: sum: 162813399
    input_simple_2.txt: sum: 48
    input_simple_3.txt: sum: 54
    input.txt: sum: 53783319
    '''
    day3Solver = Day3Solver()

    day3Solver.solve_part_1("input_simple_1.txt")
    day3Solver.solve_part_1("input.txt")

    day3Solver.solve_part_2("input_simple_2.txt")
    day3Solver.solve_part_2("input_simple_3.txt")
    day3Solver.solve_part_2("input.txt")

if __name__ == "__main__":
    main()