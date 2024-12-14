class Day13Solver:
    def __init__(self):
        self.max_presses = 100

    def parse_input(self, in_file_name, prize_offset = 0):
        f = open(in_file_name, 'r')
        lines = f.readlines()
        f.close()

        machines = []

        '''
        Button A: X+69, Y+23
        Button B: X+27, Y+71
        Prize: X=18641, Y=10279
        '''
        machine = {}
        for line in lines:
            sanitized_line = line.strip().rstrip()
            split_line = sanitized_line.split(":")

            if "button a" in sanitized_line.lower():
                x_y = split_line[1].replace(' ', '')

                x = x_y.split(',')[0].split('+')[1]
                y = x_y.split(',')[1].split('+')[1]

                machine['A'] = {}
                machine['A']['X'] = x
                machine['A']['Y'] = y

            elif "button b" in sanitized_line.lower():
                x_y = split_line[1].replace(' ', '')

                x = x_y.split(',')[0].split('+')[1]
                y = x_y.split(',')[1].split('+')[1]

                machine['B'] = {}
                machine['B']['X'] = x
                machine['B']['Y'] = y

            elif "prize" in sanitized_line.lower():
                x_y = split_line[1].replace(' ', '')

                x = x_y.split(',')[0].split('=')[1]
                y = x_y.split(',')[1].split('=')[1]

                machine['prize'] = {}
                machine['prize']['X'] = x + prize_offset
                machine['prize']['Y'] = y + prize_offset

                machines.append(machine)

            else:
                machine = {}

        return machines

    def get_all_combinations(self, machine, axis):
        all_combinations = {
            'A_value': int(machine['A'][axis]),
            'B_value': int(machine['B'][axis]),
            'combinations': []
        }

        A_list = [int(machine['A'][axis])] * 0
        B_list = [int(machine['B'][axis])] * 1
        combinations = A_list + B_list
        all_combinations['combinations'].append(combinations)

        A_list = [int(machine['A'][axis])] * 1
        B_list = [int(machine['B'][axis])] * 0
        combinations = A_list + B_list
        all_combinations['combinations'].append(combinations)

        for A in range(1, self.max_presses + 1):
            for B in range(1, self.max_presses + 1):
                A_list = [int(machine['A'][axis])] * A
                B_list = [int(machine['B'][axis])] * B

                combinations = A_list + B_list
                all_combinations['combinations'].append(combinations)

        print(f"num combinations {len(all_combinations)}")
        return all_combinations

    def get_valid_combinations(self, prize, all_combinations):
        valid_combinations = []
        for i, combination in enumerate(all_combinations):

            combination_sum = sum(combination)
            if combination_sum == int(prize):
                output = {
                    'index': i,
                    'combination': combination
                }
                valid_combinations.append(output)

            if i % 1000 == 0:
                print(f"progress... {i}")

        return valid_combinations

    def find_the_valid_machine_prizes(self, machines):
        valid_machines = []

        for machine in machines:
            all_x_combinations = self.get_all_combinations(machine, 'X')
            valid_x_combinations = self.get_valid_combinations(machine['prize']['X'], all_x_combinations['combinations'])

            all_y_combinations = self.get_all_combinations(machine, 'Y')
            valid_y_combinations = self.get_valid_combinations(machine['prize']['Y'], all_y_combinations['combinations'])

            valid_machine = {
                'valid_x': valid_x_combinations,
                'valid_y': valid_y_combinations,
                'A_x': all_x_combinations['A_value'],
                'A_y': all_y_combinations['A_value'],
                'B_x': all_x_combinations['B_value'],
                'B_y': all_y_combinations['B_value']
            }
            valid_machines.append(valid_machine)

        return valid_machines

    def find_cheapest_way_to_win(self, valid_machines):
        cheapest_machine_win = {}

        for machine_index, machine in enumerate(valid_machines):
            highest_matching_index = -1 
            cheapest = None

            for x in machine['valid_x']:
                x_index = x['index']
                for y in machine['valid_y']:
                    y_index = y['index']

                    if x_index == y_index:
                        if x_index > highest_matching_index:
                            highest_matching_index = x_index
                            cheapest = {
                                'x': x,
                                'y': y,
                                'A_x': machine['A_x'],
                                'A_y': machine['A_y'],
                                'B_x': machine['B_x'],
                                'B_y': machine['B_y']
                            }

            if cheapest:
                cheapest_machine_win[machine_index] = cheapest

        return cheapest_machine_win

    def count(self, button_press_list, A_char, B_char):
        A_count = 0
        B_count = 0

        for i in range(0, len(button_press_list)):
            if button_press_list[i] == A_char:
                A_count += 1
            elif button_press_list[i] == B_char:
                B_count += 1
            else:
                print("ERROR, DOES NOT MATCH A ({A_char}) OR B ({B_char})")

        return (A_count, B_count)

    def calculate_num_tokens(self, cheapest_way_to_win):
        tokens = 0

        for machine_index in cheapest_way_to_win:
            A_x = cheapest_way_to_win[machine_index]['A_x']
            A_y = cheapest_way_to_win[machine_index]['A_y']
            B_x = cheapest_way_to_win[machine_index]['B_x']
            B_y = cheapest_way_to_win[machine_index]['B_y']
            button_press_list = cheapest_way_to_win[machine_index]['x']['combination']

            count_A, count_B = self.count(button_press_list, A_x, B_x)

            tokens += count_A * 3 + count_B * 1

        return tokens

    def solve_part_1(self, in_file_name):
        machines = self.parse_input(in_file_name)

        valid_machines = self.find_the_valid_machine_prizes(machines)

        cheapest_way_to_win = self.find_cheapest_way_to_win(valid_machines)

        num_tokens = self.calculate_num_tokens(cheapest_way_to_win)
        print(f"{in_file_name} num_tokens {num_tokens}")

    def solve_part_2(self, in_file_name):
        machines = self.parse_input(in_file_name, prize_offset = 10000000000000)
        self.max_presses = 1000

        self.find_upper_bound(machines)

        # valid_machines = self.find_the_valid_machine_prizes(machines)

        # cheapest_way_to_win = self.find_cheapest_way_to_win(valid_machines)

        # num_tokens = self.calculate_num_tokens(cheapest_way_to_win)

        num_tokens = -1
        print(f"{in_file_name} num_tokens {num_tokens}")

def main():
    day13Solver = Day13Solver()

    day13Solver.solve_part_1("input_simple_1.txt")
    # day13Solver.solve_part_1("input.txt")

    day13Solver.solve_part_2("input_simple_1.txt")

if __name__ == "__main__":
    main()