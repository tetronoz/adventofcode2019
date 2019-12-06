from collections import deque

with open("../input/input.txt") as fp:
    map_orbits = {}
    map_parents = {}
    
    for line in fp:
        around, orbit = line.strip().split(")")
        around = str(around)
        orbit = str(orbit)
        if around in map_orbits.keys():
            map_orbits[around].append(orbit)
        else:
            map_orbits[around] = [orbit]
        map_parents[orbit] = around
        
def calculate_distance(map_orbits):
    map_distances = {}
    map_distances['COM'] = 0
    queue = deque([orbit for orbit in map_orbits['COM']])
    while queue:
        orbit = queue.popleft()
        if orbit in map_orbits.keys():
            for orbs in map_orbits[orbit]:
                queue.append(orbs)
        parent_orbit = map_parents[orbit]
        map_distances[orbit] = map_distances[parent_orbit] + 1
    return map_distances

you_orbit = map_parents['YOU']
san_orbit = map_parents['SAN']

distances = calculate_distance(map_orbits)

def count_orbital_transfers(you_orbit, san_orbit, distances):
    you_orbit_distance = distances[you_orbit]
    san_orbit_distance = distances[san_orbit]

    transfers = 0
    current_orbit_distance = you_orbit_distance

    while current_orbit_distance != san_orbit_distance:
        transfers += 1
        you_orbit = map_parents[you_orbit]
        current_orbit_distance = distances[you_orbit]

    while you_orbit != san_orbit:
        transfers += 2
        you_orbit = map_parents[you_orbit]
        san_orbit = map_parents[san_orbit]

    return transfers

print(f"total number of direct and indirect orbits: {sum(distances.values())}")
print(f"minimum number of orbital transfers: {count_orbital_transfers(you_orbit, san_orbit, distances)}")