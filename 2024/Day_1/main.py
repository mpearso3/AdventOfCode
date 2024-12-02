class Day1Solver:
    def parse_input(self, in_file_name):
        left_numbers = []
        right_numbers = []

        f = open(in_file_name, 'r')
        lines = f.readlines()
        f.close()

        for line in lines:
            sanitized_line = ' '.join(line.split())
            split_line = sanitized_line.split(' ')

            if len(split_line) == 2:
                left_number = split_line[0]
                right_number = split_line[1]

                left_numbers.append(int(left_number))
                right_numbers.append(int(right_number))
            else:
                print(f"ERROR, line did not have 2 numbers: {line}")

        return (left_numbers, right_numbers)

    def calculate_list_distance(self, left_numbers, right_numbers):
        left_numbers = sorted(left_numbers)
        right_numbers = sorted(right_numbers)

        if len(left_numbers) != len(right_numbers):
            print(f"ERROR, left and right number lists must match: len(left_numbers): {len(left_numbers)}, len(right_numbers): {len(right_numbers)}") 
            return -1

        distances = []
        for i in range(len(left_numbers)):
            distance = abs(left_numbers[i] - right_numbers[i])
            distances.append(distance)

        return sum(distances)

    def calculate_similarity_score(self, left_numbers, right_numbers):
        similarity_scores = []

        for item in left_numbers:
            count = right_numbers.count(item)
            similarity = item * count
            similarity_scores.append(similarity)

        return sum(similarity_scores)

    def solve_part_1(self, in_file_name):
        left_numbers, right_numbers = self.parse_input(in_file_name)
        total_distance = self.calculate_list_distance(left_numbers, right_numbers)
        print(f"total_distance {total_distance}")

    def solve_part_2(self, in_file_name):
        left_numbers, right_numbers = self.parse_input(in_file_name)
        similarity_score = self.calculate_similarity_score(left_numbers, right_numbers)
        print(f"similarity_score {similarity_score}")

def main():
    '''
    Example input:

    35039   67568
    61770   80134
    64079   34668
    61538   86348
    77448   73688
    56882   65376
    72415   66733
    11288   79847
    43897   20133
    56727   25055
    81287   24301
    '''

    day1Solver = Day1Solver()

    day1Solver.solve_part_1("input_simple_1.txt")
    day1Solver.solve_part_1("input.txt")

    day1Solver.solve_part_2("input_simple_1.txt")
    day1Solver.solve_part_2("input.txt")

if __name__ == "__main__":
    main()