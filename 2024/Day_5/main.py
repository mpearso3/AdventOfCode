class Day5Solver:
    def extract_page_number_rules(self, lines):
        forward_rules = {}
        reverse_rules = {}

        for line in lines:
            if '|' not in line:
                break

            sanitized_line = line.strip().rstrip()
            rule_split = sanitized_line.split('|')

            left_number  = rule_split[0]
            right_number = rule_split[1]

            if left_number not in forward_rules:
                forward_rules[left_number] = []
            forward_rules[left_number].append(right_number)

            if right_number not in reverse_rules:
                reverse_rules[right_number] = []
            reverse_rules[right_number].append(left_number)

        return forward_rules, reverse_rules

    def extract_page_updates(self, lines):
        update_lines = []

        for line in lines:
            if ',' in line:
                sanitized_line = line.strip().rstrip()
                split_line = sanitized_line.split(',')
                update_lines.append(split_line)

        return update_lines

    def check_all_forward(self, forward_rules, page_position, page, update_line):
        is_valid = True
        for i in range(page_position + 1, len(update_line)):
            if page not in forward_rules:
                return False
            if update_line[i] not in forward_rules[page]:
                is_valid = False

        return is_valid

    def check_all_reverse(self, reverse_rules, page_position, page, update_line):
        is_valid = True
        for i in range(page_position - 1, -1, -1):
            if page not in reverse_rules:
                return False
            if update_line[i] not in reverse_rules[page]:
                is_valid = False

        return is_valid

    def get_valid_update_lines(self, forward_rules, reverse_rules, update_lines):
        valid_update_lines = []

        for update_line in update_lines:
            is_valid = True
            for i, page in enumerate(update_line):
                is_valid &= self.check_all_forward(forward_rules, i, page, update_line)
                is_valid &= self.check_all_reverse(reverse_rules, i, page, update_line)
            
            if is_valid:
                valid_update_lines.append(update_line)

        return valid_update_lines

    def sum_mid_point(self, update_lines):
        sum = 0

        for update_line in update_lines:
            middle_index = int((len(update_line) - 1) / 2)
            sum += int(update_line[middle_index])

        return sum

    def solve_part_1(self, in_file_name):
        f = open(in_file_name, 'r')
        lines = f.readlines()
        f.close()

        forward_rules, reverse_rules = self.extract_page_number_rules(lines)
        update_lines = self.extract_page_updates(lines)

        valid_update_lines = self.get_valid_update_lines(forward_rules, reverse_rules, update_lines)
        sum_update_lines = self.sum_mid_point(valid_update_lines)

        print(f"{in_file_name}: sum {sum_update_lines}")

    def solve_part_2(self, in_file_name):
        pass

def main():
    day5Solver = Day5Solver()

    day5Solver.solve_part_1("input_simple_1.txt")
    day5Solver.solve_part_1("input.txt")

if __name__ == "__main__":
    main()