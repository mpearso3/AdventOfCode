import itertools

class Day7Solver:
    def parse_input_for_equations(self, lines):
        equations = []

        for line in lines:
            sanitized_line = line.strip().rstrip()
            split_line = sanitized_line.split(':')

            answer = split_line[0]
            numbers = split_line[1].strip().split(' ')

            equation = {}
            equation['answer'] = int(answer)
            equation['numbers'] = [int(x) for x in numbers]

            equations.append(equation)

        return equations

    def is_valid_equation(self, operands, numbers, answer):
        equation_answer = 0

        first_number = numbers[0]
        for i in range(1, len(numbers)):
            operand = operands[i - 1]
            number = numbers[i]

            if operand == '*':
                if equation_answer == 0:
                    equation_answer = first_number * number
                else:
                    equation_answer = equation_answer * number
            elif operand == '+':
                if equation_answer == 0:
                    equation_answer = first_number + number
                else:
                    equation_answer = equation_answer + number
            elif operand == '|':
                if equation_answer == 0:
                    equation_answer = int(str(first_number) + str(number))
                else:
                    equation_answer = int(str(equation_answer) + str(number))

        if answer == equation_answer:
            return True
        return False

    def find_valid_equations(self, equations, valid_operations):
        valid_equations = []

        for equation in equations:
            answer = equation['answer']
            numbers = equation['numbers']

            numbers_length = len(numbers)

            operaands_length = numbers_length - 1

            all_operand_options = list(itertools.product(valid_operations, repeat = operaands_length))

            for operands in all_operand_options:
                is_valid = self.is_valid_equation(operands, numbers, answer)

                if is_valid:
                    valid_equations.append(equation)
                    break

        return valid_equations

    def sum_answers(self, valid_equtions):
        sum = 0
        for equation in valid_equtions:
            answer = equation['answer']
            sum += answer

        return sum

    def solve_part_1(self, in_file_name):
        '''
        Sample input:
        190: 10 19
        3267: 81 40 27
        83: 17 5
        '''
        f = open(in_file_name, 'r')
        lines = f.readlines()
        f.close()

        valid_operations = [
            '*',
            '+'
        ]

        equations = self.parse_input_for_equations(lines)
        valid_equations = self.find_valid_equations(equations, valid_operations)

        answer_sum = self.sum_answers(valid_equations)
        print(f"{in_file_name} answer_sum {answer_sum}")

    def solve_part_2(self, in_file_name):
        f = open(in_file_name, 'r')
        lines = f.readlines()
        f.close()

        valid_operations = [
            '*',
            '+',
            '|'
        ]

        equations = self.parse_input_for_equations(lines)
        valid_equations = self.find_valid_equations(equations, valid_operations)

        answer_sum = self.sum_answers(valid_equations)
        print(f"{in_file_name} answer_sum {answer_sum}")

def main():
    day7Solver = Day7Solver()
    
    day7Solver.solve_part_1("input_simple_1.txt")
    day7Solver.solve_part_1("input.txt")
    
    day7Solver.solve_part_2("input_simple_1.txt")
    day7Solver.solve_part_2("input.txt")

if __name__ == "__main__":
    main()