class Day9Solver:
    def __init__(self):
        self.free_character = '.'

    def create_block_expansion(self, in_file_name):
        f = open(in_file_name, 'r')
        lines = f.readlines()
        f.close()

        disk_map = None
        for line in lines:
            sanitized_line = line.strip().rstrip()
            disk_map = list(sanitized_line)
            break

        block = []
        file_id = 0
        for i in range(len(disk_map)):
            if i % 2 == 0:
                file_count = int(disk_map[i])
                for _ in range(file_count):
                    block.append(file_id)

                file_id += 1

            else:
                free_count = int(disk_map[i])
                for _ in range(free_count):
                    block.append('.')

        return block

    def swap_elements(self, list_, index_1, index_2):
        list_[index_1], list_[index_2] = list_[index_2], list_[index_1]

    def is_list_fully_compressed(self, compressed):
        is_compressed = True

        free_start = False
        for item in compressed:
            if free_start:
                if item != self.free_character:
                    is_compressed = False
                    break

            if item == self.free_character:
                free_start = True

        return is_compressed

    def compress_blocks(self, block_expansion):
        compressed = list(block_expansion)

        j = len(block_expansion) - 1
        for i, item in enumerate(block_expansion):
            if self.is_list_fully_compressed(compressed):
                break

            if item == '.':
                while(compressed[j] == self.free_character):
                    j -= 1
                self.swap_elements(compressed, i, j)

        return compressed

    def filesystem_checksum(self, compressed_block):
        checksum = 0

        for i, item in enumerate(compressed_block):
            if item == self.free_character:
                break

            checksum += i * item

        return checksum

    def solve_part_1(self, in_file_name):
        block_expansion = self.create_block_expansion(in_file_name)
        compressed_block = self.compress_blocks(block_expansion)
        checksum = self.filesystem_checksum(compressed_block)

        print(f"{in_file_name}: checksum {checksum}")

    def solve_part_2(self, in_file_name):
        pass

def main():
    day9Solver = Day9Solver()

    day9Solver.solve_part_1("input_simple_1.txt")
    day9Solver.solve_part_1("input.txt")

if __name__ == "__main__":
    main()