class Day4Solver:
    def convert_input_to_2d_list(self, in_file_name):
        f = open(in_file_name, 'r')
        lines = f.readlines()
        f.close()

        list_2d = []
        for line in lines:
            sanitized_line = line.strip().rstrip()
            list_2d.append( list(sanitized_line) )
    
        return list_2d

    def search_left(self, r_i, c_i, word_search):
        if c_i > 2:
            if word_search[r_i][c_i - 1] == "M":
                if word_search[r_i][c_i - 2] == "A":
                    if word_search[r_i][c_i - 3] == "S":
                        return 1
        return 0

    def search_right(self, r_i, c_i, word_search):
        if c_i < len(word_search[r_i]) - 3:
            if word_search[r_i][c_i + 1] == "M":
                if word_search[r_i][c_i + 2] == "A":
                    if word_search[r_i][c_i + 3] == "S":
                        return 1
        return 0

    def search_up(self, r_i, c_i, word_search):
        if r_i > 2:
            if word_search[r_i - 1][c_i] == "M":
                if word_search[r_i - 2][c_i] == "A":
                    if word_search[r_i - 3][c_i] == "S":
                        return 1
        return 0

    def search_down(self, r_i, c_i, word_search):
        if r_i < len(word_search) - 3:
            if word_search[r_i + 1][c_i] == "M":
                if word_search[r_i + 2][c_i] == "A":
                    if word_search[r_i + 3][c_i] == "S":
                        return 1
        return 0

    def search_left_up(self, r_i, c_i, word_search):
        if c_i > 2:
            if r_i > 2:
                if word_search[r_i - 1][c_i - 1] == "M":
                    if word_search[r_i - 2][c_i - 2] == "A":
                        if word_search[r_i - 3][c_i - 3] == "S":
                            return 1
        return 0

    def search_right_up(self, r_i, c_i, word_search):
        if c_i < len(word_search[r_i]) - 3:
            if r_i > 2:
                if word_search[r_i - 1][c_i + 1] == "M":
                    if word_search[r_i - 2][c_i + 2] == "A":
                        if word_search[r_i - 3][c_i + 3] == "S":
                            return 1
        return 0

    def search_right_down(self, r_i, c_i, word_search):
        if c_i < len(word_search[r_i]) - 3:
            if r_i < len(word_search) - 3:
                if word_search[r_i + 1][c_i + 1] == "M":
                    if word_search[r_i + 2][c_i + 2] == "A":
                        if word_search[r_i + 3][c_i + 3] == "S":
                            return 1
        return 0

    def search_left_down(self, r_i, c_i, word_search):
        if c_i > 2:
            if r_i < len(word_search) - 3:
                if word_search[r_i + 1][c_i - 1] == "M":
                    if word_search[r_i + 2][c_i - 2] == "A":
                        if word_search[r_i + 3][c_i - 3] == "S":
                            return 1
        return 0

    def count_xmas_occurences(self, word_search):
        xmas_count = 0
        for r_i, row in enumerate(word_search):
            for c_i, letter in enumerate(row):
                if letter.upper() == 'X':
                    xmas_count += self.search_left (r_i, c_i, word_search)
                    xmas_count += self.search_right(r_i, c_i, word_search)
                    xmas_count += self.search_up   (r_i, c_i, word_search)
                    xmas_count += self.search_down (r_i, c_i, word_search)

                    xmas_count += self.search_left_up   (r_i, c_i, word_search)
                    xmas_count += self.search_right_up  (r_i, c_i, word_search)
                    xmas_count += self.search_right_down(r_i, c_i, word_search)
                    xmas_count += self.search_left_down (r_i, c_i, word_search)
        
        return xmas_count

    def search_left_up_letter(self, letter, r_i, c_i, word_search):
        if c_i > 0:
            if r_i > 0:
                if word_search[r_i - 1][c_i - 1] == letter:
                    return True
        return False

    def search_right_up_letter(self, letter, r_i, c_i, word_search):
        if c_i < len(word_search[r_i]) - 1:
            if r_i > 0:
                if word_search[r_i - 1][c_i + 1] == letter:
                    return True
        return False

    def search_right_down_letter(self, letter, r_i, c_i, word_search):
        if c_i < len(word_search[r_i]) - 1:
            if r_i < len(word_search) - 1:
                if word_search[r_i + 1][c_i + 1] == letter:
                    return True
        return False

    def search_left_down_letter(self, letter, r_i, c_i, word_search):
        if c_i > 0:
            if r_i < len(word_search) - 1:
                if word_search[r_i + 1][c_i - 1] == letter:
                    return True
        return False

    def count_double_mas_occurences(self, word_search):
        mas_count = 0
        for r_i, row in enumerate(word_search):
            for c_i, letter in enumerate(row):
                if letter.upper() == 'A':

                    valid = False

                    if self.search_left_up_letter('M', r_i, c_i, word_search):
                        if self.search_right_down_letter('S', r_i, c_i, word_search):
                            valid = True
                    if self.search_left_up_letter('S', r_i, c_i, word_search):
                        if self.search_right_down_letter('M', r_i, c_i, word_search):
                            valid = True

                    if valid:
                        if self.search_right_up_letter('M', r_i, c_i, word_search):
                            if self.search_left_down_letter('S', r_i, c_i, word_search):
                                mas_count += 1
                        if self.search_right_up_letter('S', r_i, c_i, word_search):
                            if self.search_left_down_letter('M', r_i, c_i, word_search):
                                mas_count += 1

        return mas_count

    def solve_part_1(self, in_file_name):
        word_search = self.convert_input_to_2d_list(in_file_name)

        xmas_count = self.count_xmas_occurences(word_search)
        print(f"{in_file_name}: xmas_count {xmas_count}")

    def solve_part_2(self, in_file_name):
        word_search = self.convert_input_to_2d_list(in_file_name)

        mas_count = self.count_double_mas_occurences(word_search)
        print(f"{in_file_name}: mas_count {mas_count}")

def main():
    day4Solver = Day4Solver()

    day4Solver.solve_part_1("input_simple_1.txt")
    day4Solver.solve_part_1("input.txt")

    day4Solver.solve_part_2("input_simple_1.txt")
    day4Solver.solve_part_2("input.txt")

if __name__ == "__main__":
    main()