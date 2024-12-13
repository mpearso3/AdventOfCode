class Day10Solver:
    def __init__(self):
        '''
        0 --> 1
        even number of digits --> two stones (left is left half, right is right half)
        else --> old * 2024

        Example:
            0 1 10 99 999
            blink
            1 2024 1 0 9 9 2021976

        '''
        pass

    def extract_stones(self, in_file_name):
        f = open(in_file_name, 'r')
        lines = f.readlines()
        f.close()

        stones = []
        for line in lines:
            sanitized_line = line.strip().rstrip()
            stones = sanitized_line.split(' ')
            break

        return stones

    def observe_single_blink(self, stones):
        new_stones = []

        for stone in stones:
            if stone == '0':
                new_stones.append('1')
            elif len(stone) % 2 == 0:
                middle_index = len(stone) // 2

                new_stones.append( stone[ :middle_index  ] )
                new_stones.append( stone[  middle_index: ].lstrip('0') or '0' )
            else:
                new_stones.append( str(int(stone) * 2024) )

        return new_stones    

    def observe_blinking_stones(self, stones, num_blinks):
        for blink in range(num_blinks):
            print(f"    blink {blink}")
            stones = self.observe_single_blink(stones)
        
        return stones

    def solve_part_1(self, in_file_name, num_blinks):
        initial_stones = self.extract_stones(in_file_name)

        stones = self.observe_blinking_stones(initial_stones, num_blinks)

        print(f"{in_file_name} stones {len(stones)}")

    def solve_part_2(self, in_file_name, num_blinks):
        initial_stones = self.extract_stones(in_file_name)

        count = 0
        for stone in initial_stones:
            print(f"stone {stone}")
            stones = self.observe_blinking_stones(list(stone), num_blinks)
            count += len(stones)

        print(f"{in_file_name} stones {count}")

def main():
    day10Solver = Day10Solver()

    # day10Solver.solve_part_1("input_simple_1.txt", 6)
    # day10Solver.solve_part_1("input_simple_1.txt", 25)
    # day10Solver.solve_part_1("input.txt", 25)

    day10Solver.solve_part_2("input.txt", 75)

if __name__ == "__main__":
    main()