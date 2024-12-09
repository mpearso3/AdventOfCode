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

    def get_block_size(self, compressed_blocks, id):
        size = 0

        found_id = False
        for i in range(len(compressed_blocks) - 1, -1, -1):
            if compressed_blocks[i] == id:
                found_id = True
                size += 1
            else:
                if found_id:
                    break

        return size

    def get_block_sizes(self, compressed_blocks, block_ids):
        block_sizes = {}
        for id in block_ids:
            block_sizes[id] = self.get_block_size(compressed_blocks, id)

        return block_sizes

    def get_block_ids(self, compressed):
        block_ids = {}

        for i, item in enumerate(compressed):
            if item != self.free_character:

                if item not in block_ids:
                    block_ids[item] = {}
                block_ids[item]['id_index'] = i

        block_ids = dict(sorted(block_ids.items(), key=lambda item: item[0], reverse=True))

        return block_ids

    def get_free_spaces(self, compressed):
        free_space = []

        count = 0
        start_index = 0
        for i, item in enumerate(compressed):
            if item == self.free_character:
                if count == 0:
                    start_index = i
                count += 1
            else:
                if count > 0:
                    free_space.append({'start_index': start_index, 'size': count})
                count = 0

        return free_space

    def compress_blocks_with_whole_files(self, block_expansion):
        compressed = list(block_expansion)

        block_ids = self.get_block_ids(compressed)
        block_sizes = self.get_block_sizes(compressed, block_ids)

        for id in block_ids:
            free_spaces = self.get_free_spaces(compressed)

            id_index = block_ids[id]['id_index']
            block_size = block_sizes[id]

            for free_space in free_spaces:
                start_index = free_space['start_index']
                size = free_space['size']

                if start_index < id_index:
                    if size >= block_size:
                        for i in range(block_size):
                            self.swap_elements(compressed, start_index + i, id_index - i)

        return compressed

    def filesystem_checksum(self, compressed_block):
        checksum = 0

        for i, item in enumerate(compressed_block):
            if item == self.free_character:
                continue

            checksum += i * item

        return checksum

    def solve_part_1(self, in_file_name):
        block_expansion = self.create_block_expansion(in_file_name)
        compressed_block = self.compress_blocks(block_expansion)
        checksum = self.filesystem_checksum(compressed_block)

        print(f"{in_file_name}: checksum {checksum}")

    def solve_part_2(self, in_file_name):
        block_expansion = self.create_block_expansion(in_file_name)
        compressed_block = self.compress_blocks_with_whole_files(block_expansion)
        checksum = self.filesystem_checksum(compressed_block)

        print(f"{in_file_name}: checksum {checksum}")

def main():
    day9Solver = Day9Solver()

    day9Solver.solve_part_1("input_simple_1.txt")
    day9Solver.solve_part_1("input.txt")

    day9Solver.solve_part_2("input_simple_1.txt")
    day9Solver.solve_part_2("input.txt")

if __name__ == "__main__":
    main()