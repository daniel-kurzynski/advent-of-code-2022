with open('input/day1/input.txt') as input_file:
    calories_raw  = [x.strip() for x in input_file.readlines()]

    new_elves_indices = [0] + [i + 1 for i, x in enumerate(calories_raw) if x == ""]
    calories_per_elf = [list(map(int, calories_raw[new_elves_indices[i]:new_elves_indices[i + 1] - 1])) for i in range(len(new_elves_indices) - 1)]

    sorted_sums_of_calories_per_elf = [sum(calories) for calories in calories_per_elf]
    sorted_sums_of_calories_per_elf.sort(reverse=True)

    print(f"Max calories: {sorted_sums_of_calories_per_elf[0]}")
    print(f"Some of calories of the top 3: {sum(sorted_sums_of_calories_per_elf[0:3])}")