with open('2023/Day 12/day_12.txt') as f:
    data = [line.strip('\n') for line in f.readlines()]
    
    
    
def count_arrangements(row):
    def count_possibilities(group_sizes, remaining_unknowns):
        if not group_sizes:
            return 1

        current_group_size = group_sizes[0]
        total_arrangements = 0

        for i in range(len(remaining_unknowns) - current_group_size + 1):
            substring = remaining_unknowns[i:i + current_group_size]
            if all(char == '?' for char in substring):
                new_unknowns = (
                    remaining_unknowns[:i] + '.' * current_group_size +
                    remaining_unknowns[i + current_group_size:]
                )
                total_arrangements += count_possibilities(group_sizes[1:], new_unknowns)

        return total_arrangements

    if '???' in row:
        return count_possibilities([1], row)
    else:
        group_sizes = [int(size) for size in row.split(',') if size.isdigit()]
        return count_possibilities(group_sizes, row.replace(',', ''))



total_arrangements = sum(count_arrangements(row.split(' ')[0]) for row in data)
print(total_arrangements)
