with open("../input/input_day1") as fp:
    total_fuel = 0
    for line in fp:
        module_mass = int(line.strip())
        total_fuel += module_mass//3-2

print(total_fuel)
