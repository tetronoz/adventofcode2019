def calculate_module_mass(mass):
    fuel_mass = mass//3-2
    total = fuel_mass
    while fuel_mass > 0:
        fuel_mass = fuel_mass//3 - 2
        if fuel_mass > 0:
            total += fuel_mass

    return total

with open("../input/input_day1") as fp:
    total_sum = 0
    for line in fp:
        module_mass = int(line.strip())
        total_sum += calculate_module_mass(module_mass)

print(total_sum)
